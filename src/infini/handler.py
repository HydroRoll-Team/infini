from abc import ABCMeta, abstractmethod
from .exceptions import HydroError
from .typing import Dict

__all__ = ["Result", "Handler"]


class Result(metaclass=ABCMeta):
    """规则包运行结果基类"""

    event: str
    status: bool
    exception: HydroError | None = None

    def __init__(
        self, event: str, status: bool, exception: HydroError | None = None
    ) -> None:
        self.event = event
        self.status = status
        self.exception = exception

    def ok(self):
        """规则执行期间是否产生异常"""
        return isinstance(self.exception, HydroError)


class Handler:
    """规则包业务基类"""

    name: str
    priority: int = 0

    def __init_subclass__(cls) -> None:
        handlers.regist(cls.name, cls())

    @abstractmethod
    def process(self) -> Result:
        raise NotImplementedError


class Handlers:
    """规则包业务集合"""

    _handlers: Dict[str, Handler] = {}

    def regist(self, name: str, handler: Handler) -> None:
        self._handlers[name.lower()] = handler

    def match(self, name: str) -> Handler | None:
        return self._handlers.get(name.lower())


handlers = Handlers()
