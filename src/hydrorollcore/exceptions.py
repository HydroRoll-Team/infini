class HydroError(Exception):
    """HydroRoll 异常基类"""


class RuleLoadError(HydroError):
    """规则导入错误"""
