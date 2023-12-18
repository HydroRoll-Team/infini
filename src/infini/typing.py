"""Infini 类型提示支持。

此模块定义了部分 Infini 使用的类型。
"""

from typing import (
    Dict as Dict,
    Any as Any,
    Type as Type,
    ClassVar as ClassVar,
    Generic as Generic,
    TYPE_CHECKING as TYPE_CHECKING,
    TypeVar as TypeVar,
    Callable as Callable,
    NoReturn as NoReturn,
    Awaitable as Awaitable,
)

if TYPE_CHECKING:
    from typing import Any

__all__ = ["StateT"]

StateT = TypeVar("StateT")
