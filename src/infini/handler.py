from abc import ABCMeta, abstractmethod
from .event import MatcherEvent, InfiniEvent

__all__ = ["Handler"]


class Handler:
    """规则包业务基类"""

    name: str
    priority: int = 0

    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, event: MatcherEvent) -> InfiniEvent:
        raise NotImplementedError
