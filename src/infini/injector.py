from infini.typing import Callable, T, Optional, Dict, Any
from typing import get_origin

import inspect


class Injector:
    def __init__(self) -> None:
        self.parameters: Dict[str, Any] = {}

    def inject(
        self, func: Callable[..., T], parameters: Optional[Dict[str, Any]] = None
    ) -> Callable[[], T]:
        signature = inspect.signature(func)
        _parameters = {} if parameters is None else parameters
        parameters = self.parameters.copy()
        parameters.update(_parameters)
        inject_params = {}
        for param_name, param in signature.parameters.items():
            default = None if param.default == inspect._empty else param.default
            if param_name in parameters:
                if type(parameters[param_name]) != (
                    get_origin(param.annotation) or param.annotation
                ):
                    raise ValueError(
                        f"Parameter with name '{param_name}' has a mismatch type, "
                        f"expected '{param.annotation!r}' but got '{type(parameters[param_name])!r}'."
                    )
                inject_params[param_name] = parameters[param_name]
            else:
                inject_params[param_name] = default
        bound_args = signature.bind(**inject_params)
        bound_args.apply_defaults()
        return lambda: func(*bound_args.args, **bound_args.kwargs)

    def output(
        self, func: Callable[..., T], parameters: Optional[Dict[str, Any]] = None
    ) -> T:
        return self.inject(func, parameters)()
