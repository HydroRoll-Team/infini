from abc import ABCMeta, abstractmethod
from .event import MatcherEvent
from .typing import Dict

__all__ = ["Result", "Handler"]


class Result(metaclass=ABCMeta):
    """规则包运行结果基类"""

    event: str
    status: bool
    kwargs: dict = {}

    def __init__(self, event: str, status: bool, **kwargs) -> None:
        self.event = event
        self.status = status
        self.kwargs = kwargs


class Handler:
    """规则包业务基类"""

    name: str
    priority: int = 0

    def __init_subclass__(cls) -> None:
        handlers.regist(cls.name, cls())

    @abstractmethod
    def process(self, event: MatcherEvent) -> Result:
        raise NotImplementedError


class Handlers:
    """规则包业务集合"""

    _handlers: Dict[str, Handler] = {}

    def regist(self, name: str, handler: Handler) -> None:
        self._handlers[name.lower()] = handler

    def match(self, name: str) -> Handler | None:
        return self._handlers.get(name.lower())


handlers = Handlers()
