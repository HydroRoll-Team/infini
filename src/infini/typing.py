from typing import (
    Dict as Dict,
    List as List,
    Any as Any,
    Generic as Generic,
    Callable as Callable,
    Literal as Literal,
    Sequence as Sequence,
    overload as overload,
    TypeVar,
    TypedDict,
    Union,
)
from types import ModuleType as ModuleType, GeneratorType as GeneratorType
from . import router, input, output

T = TypeVar("T")


class RouterType(TypedDict):
    priority: int
    router: router.Router
    handler: Callable[["input.Input"], Union["input.Input", "output.Output"]]
