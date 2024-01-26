from infini.input import Input
from infini.output import Output
from infini.typing import List, RouterType, Callable
from infini.queue import EventQueue


class Handler:
    handlers: List[RouterType]

    def input(self, input: Input):
        queue = self.match(input.get_plain_text())
        if queue.is_empty():
            yield Output.empty()
            return
        while not queue.is_empty():
            output = queue.pop()(input)
            yield output
            if output.block:
                return

    def match(self, text: str) -> EventQueue[Callable[[Input], Output]]:
        queue = EventQueue()

        for handler in self.handlers:
            if handler["router"].match(text):
                queue.push(handler["priority"], handler["handler"])

        return queue
