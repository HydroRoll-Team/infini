from abc import ABCMeta


class Event(metaclass=ABCMeta):
    """事件基类"""

    name: str
    output: str

    def __init__(self, name: str, output: str) -> None:
        self.name = name
        self.output = output
