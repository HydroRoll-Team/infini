from abc import ABCMeta, abstractmethod


class Rule(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @classmethod
    def __subclasshook__(cls, other):
        if cls is Rule:
            return hasattr(other, 'run') and callable(getattr(other, 'run'))
        return NotImplemented

    @abstractmethod
    async def run(self):
        pass
