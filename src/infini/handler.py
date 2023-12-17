"""Infini Handler

此类是所有规则包业务类的基类。
每个规则包业务类都需要定义一个名为 process 的抽象方法, 用于接收和处理传入的 MatcherEvent 事件，并返回一个 InfiniEvent 事件。
此外，每个规则包业务类还可以定义一个名为 priority 的类属性，用于指定该业务类的优先级。优先级越高，该业务类处理事件的顺序越靠前。
"""

from abc import ABC, ABCMeta, abstractmethod
from enum import Enum
from typing import ClassVar, Generic, NoReturn, Optional, final

from infini.exceptions import SkipException, StopException
from infini.typing import StateT
from infini.event import MatcherEvent, InfiniEvent

__all__ = ["Handler", "HandlerLoadType"]


class HandlerLoadType(Enum):
    """规则包加载类型。"""

    DIR = "dir"
    NAME = "name"
    FILE = "file"
    CLASS = "class"


class Handler(ABC, Generic[StateT]):
    """规则包业务基类"""

    priority: ClassVar[int] = 0
    block: ClassVar[bool] = False

    def __init_state__(self) -> Optional[StateT]:
        """初始化规则包状态。"""

    @final
    @property
    def name(self) -> str:
        """规则包名称。"""
        return self.__class__.__name__

    @final
    def stop(self) -> NoReturn:
        """停止当前事件传播。"""
        raise StopException

    @final
    def skip(self) -> NoReturn:
        """跳过自身继续当前事件传播。"""
        raise SkipException

    @abstractmethod
    def process(self, event: MatcherEvent) -> InfiniEvent:
        raise NotImplementedError
