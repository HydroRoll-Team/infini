from infini.exceptions import UnknownMessageEvent
from infini.handler import Handler
from infini.typing import Dict

import re


class Loader:
    ...


class Register:
    ...


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


class Handlers:
    """规则包业务集合"""

    _handlers: Dict[str, Handler] = {}

    def regist(self, name: str, handler: Handler) -> None:
        self._handlers[name.lower()] = handler

    def match(self, name: str) -> Handler | None:
        return self._handlers.get(name.lower())


handlers = Handlers()
events = Events()
