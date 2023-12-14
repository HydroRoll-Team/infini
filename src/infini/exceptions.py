class HydroError(Exception):
    """HydroRoll 异常基类"""


class RuleLoadError(HydroError):
    """规则导入错误"""


class EventError(HydroError):
    """事件处理时异常"""


class UnknownMatcherEvent(EventError):
    """未知的给入实现"""
