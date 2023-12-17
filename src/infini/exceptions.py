class HydroError(Exception):
    """HydroRoll 异常基类"""


class LoadError(HydroError):
    """规则包导入错误"""


class PackageNotFound(LoadError):
    """规则包不存在"""


class EventLoadError(LoadError, RuntimeError):
    """事件声明导入失败"""


class HandlerLoadError(LoadError, RuntimeError):
    """业务函数导入失败"""


class EventError(HydroError):
    """事件处理时异常"""


class UnknownEvent(EventError):
    """未知事件"""


class UnknownMatcherEvent(UnknownEvent):
    """未知的给入实现"""


class UnknownMessageEvent(UnknownEvent):
    """未知的给出实现"""


class UnsupportedError(EventError, RuntimeError):
    """方法未被支持"""
