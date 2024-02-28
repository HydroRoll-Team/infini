from infini.typing import Callable, T, Optional, Dict, Any

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
                if not isinstance(parameters[param_name], param.annotation):
                    raise ValueError(
                        f"Parameter with name '{param_name}' has a mismatch type."
                    )
                inject_params[param_name] = parameters[param_name]
            else:
                for parameter in parameters:
                    if isinstance(parameter, param.annotation):
                        inject_params[param_name] = parameter
                        break
                else:
                    inject_params[param_name] = default
        bound_args = signature.bind(**inject_params)
        bound_args.apply_defaults()
        return lambda: func(*bound_args.args, **bound_args.kwargs)

    def output(
        self, func: Callable[..., T], parameters: Optional[Dict[str, Any]] = None
    ) -> T:
        return self.inject(func, parameters)()
