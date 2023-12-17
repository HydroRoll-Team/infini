from abc import ABCMeta, abstractmethod
from .event import MatcherEvent, InfiniEvent

__all__ = ["Handler"]


class Handler(metaclass=ABCMeta):
    """规则包业务基类"""

    name: str
    priority: int = 0

    @abstractmethod
    def process(self, event: MatcherEvent) -> InfiniEvent:
        raise NotImplementedError
