"""Infini Matcher

用于处理和匹配事件。
"""

from .register import Register, register
from .event import MatcherEvent
from .handler import Handler
from .exceptions import UnknownMatcherEvent


class Matcher:
    """事件处理单元"""

    register: Register

    def __init__(self, _register: Register | None = None) -> None:
        self.register = _register or register

    def match(self, name: str) -> Handler:
        if handler := self.register.handlers.match(name):
            return handler if isinstance(handler, Handler) else handler()
        else:
            raise UnknownMatcherEvent(f"未知的规则包: {name}")

    def run(self, event: MatcherEvent) -> str:
        callback_event = self.match(event.name).process(event)
        return self.register.events.process(
            callback_event.name,
            **callback_event.kwargs or callback_event.kwargs,
        )


matcher = Matcher()
