from abc import ABCMeta, abstractmethod
from enum import Enum

__all__ = ["RuleLoadType", "Rule"]


class RuleLoadType(Enum):
    """The Type Of Rules To Be Loaded"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"


class Rule(metaclass=ABCMeta):
    """规则基类"""

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def run(self):
        raise NotImplementedError
