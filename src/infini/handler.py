from infini.input import Input
from infini.output import Output
from infini.typing import List, Any, RouterType, Callable, Generator
from infini.queue import EventQueue


class Handler:
    handlers: List[RouterType]

    def input(self, input: Input):
        if (queue := self.match(input.get_plain_text())).is_empty():
            yield Output.empty()
            return
        while not queue.is_empty():
            if isinstance(stream := queue.pop()(input), Generator):
                for output in stream:
                    yield output
                    if output.block:
                        return
            else:
                yield stream
                if stream.block:
                    return

    def match(
        self, text: str
    ) -> EventQueue[Callable[[Input], Output | Generator[Output, Any, None]]]:
        queue = EventQueue()

        for handler in self.handlers:
            if handler["router"].match(text):
                queue.push(handler["priority"], handler["handler"])

        return queue
