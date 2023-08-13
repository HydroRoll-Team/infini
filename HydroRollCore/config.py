"""HydroRollCore 配置。

HydroRollCore 使用 [pydantic](https://pydantic-docs.helpmanual.io/) 来读取配置。
"""
from typing import Set, Union

from pydantic import Extra, Field, BaseModel, DirectoryPath

__all__ = [
    "ConfigModel",
    "LogConfig",
    "CoreConfig",
    "RuleConfig",
    "MainConfig",
]


class ConfigModel(BaseModel):
    """HydroRollCore 配置模型。

    Attributes:
        __config_name__: 配置名称。
    """

    __config_name__: str

    class Config:
        extra = Extra.allow


class LogConfig(ConfigModel):
    """HydroRollCore 日志相关设置。

    Attributes:
        level: 日志级别。
        verbose_exception: 详细的异常记录，设置为 True 时会在日志中添加异常的 Traceback。
    """

    level: Union[str, int] = "DEBUG"
    verbose_exception: bool = False


class CoreConfig(ConfigModel):
    """Core 配置。

    Attributes:
        rules: 将被加载的规则书列表，将被 `Core` 类的 `load_rules()` 方法加载。
        rule_dirs: 将被加载的规则书目录列表，将被 `Core` 类的 `load_rules_from_dirs()` 方法加载。
        log: HydroRollCore 日志相关设置。
    """

    rules: Set[str] = Field(default_factory=set)
    rule_dirs: Set[DirectoryPath] = Field(default_factory=set)
    log: LogConfig = LogConfig() # type: ignore


class RuleConfig(ConfigModel):
    """规则书配置。"""


class DebugConfig(ConfigModel):
    """是否打印事件配置。"""


class MainConfig(ConfigModel):
    """HydroRollCore 配置。

    Attributes:
        core: HydroRollCore 的主要配置。
    """

    core: CoreConfig = CoreConfig() # type: ignore
    rule: RuleConfig = RuleConfig() # type: ignore

    class Config:
        extra = Extra.allow