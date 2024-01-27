from infini.input import Input
from infini.output import Output
from infini.router import Contains, Router
from infini.typing import List, Dict, Any, Callable, RouterType
from functools import wraps


class Register:
    pre_interceptors: List[RouterType]
    handlers: List[RouterType]
    events: Dict[str, str]
    global_variables: Dict[str, str | Callable]
    interceptors: List[RouterType]

    def __init__(self) -> None:
        self.pre_interceptors = []
        self.handlers = []
        self.events = {}
        self.global_variables = {}
        self.interceptors = []

    def pre_interceptor(self, router: Router | str, priority: int = 0):
        def decorator(func):
            @wraps(func)
            def wrapper(input: Input) -> Input | Output:
                return func(input)

            self.pre_interceptors.append(
                {
                    "priority": priority,
                    "router": Contains(router)
                    if isinstance(router, str)
                    else router,
                    "handler": wrapper,
                }
            )
            return wrapper

        return decorator

    def handler(self, router: Router | str, priority: int = 0):
        def decorator(func):
            @wraps(func)
            def wrapper(input: Input) -> Output:
                return func(input)

            self.handlers.append(
                {
                    "priority": priority,
                    "router": Contains(router)
                    if isinstance(router, str)
                    else router,
                    "handler": wrapper,
                }
            )
            return wrapper

        return decorator

    def regist_textevent(self, name: str, text: str):
        self.events[name] = text

    def regist_variable(self, name: str, data: Any):
        self.global_variables[name] = data

    def dynamic_variable(self, name: str | None = None):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs) -> str:
                return func(*args, **kwargs)

            self.global_variables[name or func.__name__] = wrapper
            return wrapper

        return decorator

    def interceptor(self, router: Router | str, priority: int = 0):
        def decorator(func):
            @wraps(func)
            def wrapper(input: Input) -> Input | Output:
                return func(input)

            self.interceptors.append(
                {
                    "priority": priority,
                    "router": Contains(router)
                    if isinstance(router, str)
                    else router,
                    "handler": wrapper,
                }
            )
            return wrapper

        return decorator
