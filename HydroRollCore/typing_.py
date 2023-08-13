"""HydroRollCore 类型提示支持。

此模块定义了部分 HydroRollCore 使用的类型。
"""

from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from HydroRollCore.core import Core  # noqa
    from HydroRollCore.rule import Rule  # noqa
    from HydroRollCore.config import ConfigModel  # noqa

__all__ = [
    "T_State",
    "T_Core",
    "T_Rule",
    "T_Config"
]

T_State = TypeVar("T_State")
T_Core = TypeVar("T_Core", bound="Core")
T_Rule = TypeVar("T_Rule", bound="Rule")
T_Config = TypeVar("T_Config", bound="ConfigModel")