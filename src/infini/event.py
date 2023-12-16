from .typing import Dict
from .exceptions import UnknownMessageEvent

import re

__all__ = ["MessageEvent", "events"]


class InfiniEvent:
    """Inifni 事件基类"""

    name: str


class Events:
    """事件集合"""

    _events: Dict[str, str] = {}

    def regist(self, name: str, output: str) -> None:
        self._events[name.lower()] = output

    def process(self, name: str, **kwargs) -> str:
        if string := self._events.get(name.lower()):
            return self._format(string, **kwargs)
        raise UnknownMessageEvent(f"事件[{name.lower()}]不存在！")

    def _format(self, string: str, **kwargs):
        pattern = r"{(.*?)}"
        values = re.findall(pattern, string)
        for value in values:
            kwarg = kwargs.get(value)
            value = kwarg if kwarg else ""
            string = re.sub(pattern, value, string)
        return string


class MessageEvent(InfiniEvent):
    """Message 事件"""

    name: str
    output: str

    def __repr__(self) -> str:
        return f"<MessageEvent [{self.name}]>"


class WorkflowEvent(InfiniEvent):
    """Workflow 事件"""

    name: str
    kwargs: dict

    def __repr__(self) -> str:
        return f"<WorkflowEvent [{self.name}]>"


class MatcherEvent(InfiniEvent):
    """Matcher 事件"""

    name: str
    prefix: str
    string: str
    kwargs: dict

    def __init__(self, event_name: str, string: str | None = None, **kwargs):
        self.name = event_name
        self.string = string or ""
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return f"<MatcherEvent [{self.name}]>"


events = Events()
