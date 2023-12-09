from abc import ABCMeta, abstractmethod
from enum import Enum

__all__ = ["RuleLoadType", "Rule"]


class RuleLoadType(Enum):
    """The Type Of Rules To Be Loaded"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"


class Result(metaclass=ABCMeta):
    """规则检定结果基类"""

    event: str


class Dice(metaclass=ABCMeta):
    """掷骰基类"""

    roll_string: str
    db: str
    outcome: int

    def __repr__(self) -> str:
        return f'<HydroDice "{self.db.upper()}">'

    def __str__(self) -> str:
        return self.db.upper()

    @abstractmethod
    def parse(self) -> "Dice":
        raise NotImplementedError

    @abstractmethod
    def roll(self) -> int:
        raise NotImplementedError


class Rule(metaclass=ABCMeta):
    """规则基类"""

    name: str
    priority: int = 0

    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def check(self) -> Result:
        raise NotImplementedError
