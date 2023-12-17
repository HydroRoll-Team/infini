from pathlib import Path
from .exceptions import UnknownMessageEvent
from .handler import Handler
from .event import InfiniEvent
from .typing import Dict
from .exceptions import LoadError, EventLoadError, HandlerLoadError

import re
import sys
import importlib
import inspect


class Loader:
    """加载器"""

    name: str
    meta_path: Path
    events: dict
    handlers: dict

    def __init__(self, meta_path: Path | str) -> None:
        if isinstance(meta_path, str):
            self.meta_path = Path(meta_path).resolve()
        else:
            self.meta_path = meta_path.resolve()
        self.name = self.meta_path.name
        self.events = {}
        self.handlers = {}

    def load(self) -> None:
        sys.path.append(str(self.meta_path))
        try:
            importlib.import_module(f"{self.name}")
        except Exception as error:
            raise LoadError(f"规则包[{self.name}]导入失败: {error}") from error

        try:
            event_module = importlib.import_module(f"{self.name}.event")
            events = [
                cls[1]
                for cls in inspect.getmembers(event_module, inspect.isclass)
                if issubclass(cls[1], InfiniEvent)
                and not cls[1].__module__.startswith("infini")
            ]
            for event in events:
                self.events[event.__dict__["name"]] = event
        except Exception as error:
            raise EventLoadError(f"规则包[{self.name}]事件导入失败: {error}") from error

        try:
            handler_module = importlib.import_module(f"{self.name}.handler")
            events = [
                cls[1]
                for cls in inspect.getmembers(handler_module, inspect.isclass)
                if issubclass(cls[1], InfiniEvent)
                and not cls[1].__module__.startswith("infini")
            ]
            for event in events:
                self.handlers[event.__dict__["name"]] = event
        except Exception as error:
            raise HandlerLoadError(f"规则包[{self.name}]业务函数导入失败: {error}") from error

        sys.path.remove(str(self.meta_path))


class Register:
    """注册器"""

    events: Dict[str, str]


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
