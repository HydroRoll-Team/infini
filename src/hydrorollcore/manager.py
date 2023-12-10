from .event import Events, events
from .logging import logger
from .typing import Dict


class Manager:
    """事件处理单元"""

    events: Events

    def __init__(self, _events: Events = None) -> None:
        self.events = _events if _events else events

    def roll(self):
        ...


manager = Manager()
