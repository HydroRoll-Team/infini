from .event import MatcherEvent, Events, events
from .handler import Handlers, Handler, handlers
from .exceptions import UnknownMatcherEvent


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
        result = self.match(event.name).process(event)
        return self.events.process(
            result.event, **result.kwargs if result.kwargs else event.kwargs
        )


matcher = Matcher()
