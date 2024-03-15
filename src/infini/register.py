from infini.doc import Doc
from infini.typing import List, Dict, Any, Callable, RouterType, Optional, Union, Type
from infini.input import Input
from infini.output import Output
from infini.router import Contains, Router
from infini.generator import BaseGenerator
from functools import wraps


class Register:
    pre_interceptors: List[RouterType]
    handlers: List[RouterType]
    events: Dict[str, str]
    global_variables: Dict[str, Union[str, Callable]]
    interceptors: List[RouterType]
    generators: Dict[str, BaseGenerator]

    doc: Doc

    def __init__(self) -> None:
        self.pre_interceptors = []
        self.handlers = []
        self.events = {}
        self.global_variables = {}
        self.interceptors = []
        self.generators = {}
        self.doc = Doc()

    def pre_interceptor(
        self,
        router: Union[Router, str],
        *,
        priority: int = 0,
        namespace: Optional[str] = None,
        usage: Optional[str] = None,
        description: Optional[str] = None,
        epilog: Optional[str] = None,
    ):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs) -> Union[Input, Output]:
                return func(*args, **kwargs)

            _router = Contains(router) if isinstance(router, str) else router
            self.pre_interceptors.append(
                {
                    "priority": priority,
                    "router": _router,
                    "handler": wrapper,
                }
            )
            self.doc.pre_interceptors[
                namespace or _router.namespace or func.__name__
            ] = {
                "usage": usage,
                "description": description,
                "epilog": epilog,
            }
            return wrapper

        return decorator

    def handler(
        self,
        router: Union[Router, str],
        *,
        priority: int = 0,
        namespace: Optional[str] = None,
        usage: Optional[str] = None,
        description: Optional[str] = None,
        epilog: Optional[str] = None,
    ):
        """注册一个业务函数"""

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs) -> Output:
                return func(*args, **kwargs)

            _router = Contains(router) if isinstance(router, str) else router
            self.handlers.append(
                {
                    "priority": priority,
                    "router": _router,
                    "handler": wrapper,
                }
            )
            self.doc.handlers[namespace or _router.namespace or func.__name__] = {
                "usage": usage,
                "description": description,
                "epilog": epilog,
            }
            return wrapper

        return decorator

    def register_textevent(
        self, name: str, text: str, *, description: Optional[str] = None
    ):
        self.events[name] = text
        self.doc.events[name] = {
            "usage": None,
            "description": description,
            "epilog": None,
        }

    def register_variable(
        self,
        name: str,
        data: Any,
        *,
        usage: Optional[str] = None,
        description: Optional[str] = None,
    ):
        self.global_variables[name] = data
        self.doc.global_variables[name] = {
            "usage": usage,
            "description": description,
            "epilog": None,
        }

    def dynamic_variable(
        self,
        name: Optional[str] = None,
        *,
        usage: Optional[str] = None,
        description: Optional[str] = None,
    ):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs) -> str:
                return func(*args, **kwargs)

            self.global_variables[name or func.__name__] = wrapper
            self.doc.global_variables[name or func.__name__] = {
                "usage": usage,
                "description": description,
                "epilog": None,
            }
            return wrapper

        return decorator

    def interceptor(
        self,
        router: Union[Router, str],
        *,
        priority: int = 0,
        namespace: Optional[str] = None,
        usage: Optional[str] = None,
        description: Optional[str] = None,
        epilog: Optional[str] = None,
    ):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs) -> Union[Input, Output]:
                return func(*args, **kwargs)

            _router = Contains(router) if isinstance(router, str) else router
            self.interceptors.append(
                {
                    "priority": priority,
                    "router": _router,
                    "handler": wrapper,
                }
            )
            self.doc.interceptors[namespace or _router.namespace or func.__name__] = {
                "usage": usage,
                "description": description,
                "epilog": epilog,
            }
            return wrapper

        return decorator

    def register_generator(
        self, generator: Union[BaseGenerator, Type[BaseGenerator]]
    ) -> None:
        if not isinstance(generator, BaseGenerator):
            generator = generator()
        self.generators[generator.type] = generator
