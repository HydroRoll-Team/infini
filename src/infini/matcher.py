from .event import Events, events
from .handler import Handlers, Handler, Result, handlers
from .exceptions import UnknownMatcherEvent
from .typing import Callable
from .logging import logger


class MatcherEvent:
    """Matcher 事件"""

    name: str
    kwargs: dict

    def __init__(self, name: str, **kwargs):
        self.name = name
        self.kwargs = kwargs

    def __repr__(self) -> str:
        return f"<MatcherEvent [{self.name}]>"


class Matcher:
    """事件处理单元"""

    events: Events
    handlers: Handlers

    def __init__(
        self, _events: Events | None = None, _handlers: Handlers | None = None
    ) -> None:
        self.events = _events if _events else events
        self.handlers = _handlers if _handlers else handlers

    def match(self, name: str) -> Handler:
        if handler := self.handlers.match(name):
            return handler
        else:
            raise UnknownMatcherEvent(f"未知的规则包: {name}")

    def run(self, event: MatcherEvent) -> str:
        logger.debug(f"开始处理事件: {event.name}...")
        result = self.match(event.name).process()
        return self.events.process(result.event, **event.kwargs)


matcher = Matcher()
