"""Infini Handler

此类是所有规则包业务类的基类。
每个规则包业务类都需要定义一个名为 process 的抽象方法, 用于接收和处理传入的 MatcherEvent 事件，并返回一个 InfiniEvent 事件。
此外，每个规则包业务类还可以定义一个名为 priority 的类属性，用于指定该业务类的优先级。优先级越高，该业务类处理事件的顺序越靠前。
"""

from abc import ABCMeta, abstractmethod
from enum import Enum
from .event import MatcherEvent, InfiniEvent

__all__ = ["Handler", "HandlerLoadType"]


class HandlerLoadType(Enum):
    """规则包加载类型。"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"


class Handler:
    """规则包业务基类"""

    name: str
    priority: int = 0

    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, event: MatcherEvent) -> InfiniEvent:
        raise NotImplementedError
