"""Infini 异常处理模块

此模块定义了 Infini 项目中所有的自定义异常类。
规则包作者后续实现的每个异常类都应该继承自 InfiniBaseError。
"""


class EventException(BaseException):
    """事件处理过程中由规则包抛出的异常, 用于控制事件的传播, 会被 Infini 自动捕获并处理。"""


class SkipException(EventException):
    """跳过当前规则包继续当前事件传播。"""


class StopException(EventException):
    """停止当前事件传播。"""


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
