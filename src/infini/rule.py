from abc import ABCMeta, abstractmethod
from enum import Enum
from .exceptions import HydroError
from .typing import Dict

__all__ = ["RuleLoadType", "Result", "Dice", "Rule"]


class RuleLoadType(Enum):
    """The Type Of Rules To Be Loaded"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"


class Result(metaclass=ABCMeta):
    """规则检定结果基类"""

    event: str
    status: bool
    exception: HydroError | None = None

    def __init__(self, event: str, status: bool, exception: HydroError | None) -> None:
        self.event = event
        self.status = status
        self.exception = exception

    def ok(self):
        """规则执行期间是否产生异常"""
        return isinstance(self.exception, HydroError)


class Dice(metaclass=ABCMeta):
    """掷骰基类"""

    roll_string: str
    db: str
    outcome: int

    def __repr__(self) -> str:
        return f'<HydroDice "{self.db.upper()}">'

    def __str__(self) -> str:
        return self.db.upper()

    def __int__(self) -> int:
        return self.outcome

    @abstractmethod
    def parse(self) -> "Dice":
        """解析传入的掷骰字符串`roll_string`，返回一个`Dice`对象"""
        raise NotImplementedError

    @abstractmethod
    def roll(self) -> int:
        """掷骰方法，返回掷骰结果"""
        raise NotImplementedError


class Rule(metaclass=ABCMeta):
    """规则基类"""

    name: str
    dices: Dict[str, str] = {}
    priority: int = 0

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def check(self, dice: Dice) -> Result:
        raise NotImplementedError
