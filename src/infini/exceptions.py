"""Infini 异常处理模块

此模块定义了 Infini 项目中所有的自定义异常类。
规则包作者后续实现的每个异常类都应该继承自 RulePackageException。
"""


class EventException(BaseException):
    """事件处理过程中由规则包抛出的异常, 用于控制事件的传播, 会被 Infini 自动捕获并处理。"""


class SkipException(EventException):
    """跳过当前规则包继续当前事件传播。"""


class StopException(EventException):
    """停止当前事件传播。"""


class InfiniException(Exception):
    """Infini 异常基类"""


class RulePackageException(InfiniException):
    """由规则包抛出的异常基类, 所有规则包抛出的异常都应该继承此类。"""


class LoadError(InfiniException):
    """加载规则包错误, 找不到指定的规则包或事件声明有误导致运行时错误时抛出。"""


class PackageNotFound(LoadError):
    """规则包不存在时错误, """


class EventLoadError(LoadError, RuntimeError):
    """事件声明导入失败"""


class HandlerLoadError(LoadError, RuntimeError):
    """业务函数导入失败"""


class UnknownException(BaseException):
    """未知异常基类"""


class UnknownMatcherEvent(UnknownException):
    """未知的给入实现"""


class UnknownMessageEvent(UnknownException):
    """未知的给出实现"""


class UnsupportedError(EventException, RuntimeError):
    """方法未被支持"""
