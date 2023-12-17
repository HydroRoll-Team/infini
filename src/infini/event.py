"""Infini 事件模块

此模块定义了 Infini 的事件类，包括 InfiniEvent, MessageEvent, WorkflowEvent 和 MatcherEvent。
这些事件类用于在 Infini 框架中处理各种事件。
"""

from abc import ABCMeta, abstractmethod
from .typing import Dict, Any

__all__ = [
    "InfiniEvent",
    "MessageEvent",
    "WorkflowEvent",
    "MatcherEvent",
]


class InfiniEvent(metaclass=ABCMeta):
    """Infini 事件基类"""

    name: str
    kwargs: Dict[str, Any]

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError

    def get_event_name(self) -> str:
        return self.name


class MessageEvent(InfiniEvent):
    """Message 事件"""

    name: str
    output: str
    kwargs: Dict[str, Any]

    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.kwargs = kwargs

    def __str__(self) -> str:
        return f"<MessageEvent [{self.name}]>"

    def __repr__(self) -> str:
        return self.__str__()


class WorkflowEvent(InfiniEvent):
    """Workflow 事件"""

    name: str
    kwargs: Dict[str, Any]

    def __init__(self, name: str, **kwargs) -> None:
        self.name = name
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return f"<WorkflowEvent [{self.name}]>"

    def __eq__(self, __value: object) -> bool:
        if __value is str:
            return self.name == __value
        if isinstance(__value, WorkflowEvent):
            return self.name == __value.name and self.kwargs == __value.kwargs
        return False


class MatcherEvent(InfiniEvent):
    """Matcher 事件"""

    name: str
    prefix: str
    string: str
    kwargs: Dict[str, Any]

    def __init__(
        self,
        event_name: str,
        prefix: str | None = None,
        string: str | None = None,
        **kwargs,
    ):
        self.name = event_name
        self.prefix = prefix or ""
        self.string = string or ""
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return f"<MatcherEvent [{self.name}]>"

    def get_prefix(self):
        return self.prefix

    def get_plain_text(self):
        return self.string
