from .typing import Dict
from .log import logger

import re

__all__ = ["Event", "events"]


class Events:
    """事件集合"""

    _events: Dict[str, str] = {}

    def regist(self, name: str, output: str) -> None:
        self._events[name.lower()] = output

    def process(self, name: str, **kwargs) -> str:
        string = self._events.get(name.lower())
        if not string:
            logger.warning(f"事件[{name.lower()}]不存在，将返回空字符串！")
            return ""
        else:
            return self._format(string, **kwargs)

    def _format(self, string: str, **kwargs):
        pattern = r"{(.*?)}"
        values = re.findall(pattern, string)
        for value in values:
            kwarg = kwargs.get(value)
            value = kwarg if kwarg else ""
            string = re.sub(pattern, value, string)
        return string


class Event:
    """事件基类"""

    name: str
    output: str

    def __init_subclass__(cls) -> None:
        events.regist(cls.name, cls.output)


events = Events()
