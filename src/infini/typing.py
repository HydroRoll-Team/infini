from typing import (
    Dict as Dict,
    List as List,
    Any as Any,
    Optional as Optional,
    Generic as Generic,
    Callable as Callable,
    Literal as Literal,
    Sequence as Sequence,
    Generator as Generator,
    overload as overload,
    TypeVar,
    TypedDict,
    Union,
)
from types import ModuleType as ModuleType, GeneratorType as GeneratorType
from . import router, input, output

T = TypeVar("T")
Stream = Union["input.Input[Any]", "output.Output"]
OutputGenerator = Generator["output.Output", Any, None]


class RouterType(TypedDict):
    priority: int
    router: router.Router
    handler: Callable[..., Union[Stream, OutputGenerator]]
