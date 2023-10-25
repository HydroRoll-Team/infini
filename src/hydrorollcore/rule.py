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
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def __subclasshook__(cls, other):
        if cls is Rule:
            return hasattr(other, "run") and callable(getattr(other, "run"))
        return NotImplemented

    @abstractmethod
    async def run(self):
        pass
