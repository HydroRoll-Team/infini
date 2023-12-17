from pathlib import Path
from .exceptions import UnsupportedError
from .handler import Handler
from .event import InfiniEvent, MessageEvent, WorkflowEvent
from .typing import Dict, Type
from .exceptions import LoadError, EventLoadError, HandlerLoadError, UnknownEvent

import re
import sys
import importlib
import inspect


class Loader:
    """Infini 事件加载器"""

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
                self.events[f"{self.name}.{event.__dict__['name']}"] = event
        except Exception as error:
            raise EventLoadError(f"规则包[{self.name}]事件导入失败: {error}") from error

        try:
            handler_module = importlib.import_module(f"{self.name}.handler")
            handlers = [
                cls[1]
                for cls in inspect.getmembers(handler_module, inspect.isclass)
                if issubclass(cls[1], Handler)
                and not cls[1].__module__.startswith("infini")
            ]
            for handler in handlers:
                self.handlers[f"{self.name}.{handler.__dict__['name']}"] = handler
        except Exception as error:
            raise HandlerLoadError(f"规则包[{self.name}]业务函数导入失败: {error}") from error

        sys.path.remove(str(self.meta_path))


class Events:
    """事件集合"""

    _events: Dict[str, Type[InfiniEvent]]

    def __init__(self) -> None:
        self._events = {}

    def regist(self, name: str, event: Type[InfiniEvent]) -> None:
        self._events[name.lower()] = event

    def update(self, _events: dict) -> None:
        self._events.update(_events)

    def _process(self, event: Type[InfiniEvent], **kwargs) -> str:
        if issubclass(event, MessageEvent):
            return self._format(event.__dict__["output"], **kwargs)
        elif issubclass(event, WorkflowEvent):
            raise UnsupportedError
        else:
            raise UnsupportedError

    def process(self, name: str, **kwargs) -> str:
        if event := self._events.get(name.lower()):
            return self._process(event, **kwargs)
        raise UnknownEvent(f"事件[{name.lower()}]不存在！")

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

    def update(self, _events: dict) -> None:
        self._handlers.update(_events)

    def match(self, name: str) -> Handler | None:
        return self._handlers.get(name.lower())


class Register:
    """注册器"""

    events: Events
    handlers: Handlers

    def __init__(self) -> None:
        self.events = Events()
        self.handlers = Handlers()

    def regist(self, meta_path: Path | str | None = None):
        _loader = Loader(meta_path if meta_path else ".")
        _loader.load()
        self.events.update(_loader.events)
        self.handlers.update(_loader.handlers)


register = Register()
