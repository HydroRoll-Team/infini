from infini.input import Input
from infini.output import Output
from infini.typing import List, Any, RouterType, Callable, Generator
from infini.queue import EventQueue


class Interceptor:
    interceptors: List[RouterType]

    def input(self, input: Input) -> Generator[Output | Input, Any, None]:
        queue = self.match(input.get_plain_text())
        while not queue.is_empty():
            if isinstance(stream := queue.pop()(input), Generator):
                for outcome in stream:
                    if isinstance(outcome, Input):
                        input = outcome
                        break
                    yield outcome
                    if outcome.block:
                        return
            else:
                if stream is None:
                    yield Output.empty()
                    return
                if isinstance(stream, Output):
                    yield stream
                    if stream.block:
                        return
                    continue
                input = stream
        yield input

    def output(
        self, output_text: str
    ) -> Generator[Output | str, Any, None]:
        input = Input(output_text)
        queue = self.match(input.get_plain_text())
        while not queue.is_empty():
            if isinstance(stream := queue.pop()(input), Generator):
                for outcome in stream:
                    if isinstance(outcome, Input):
                        input = outcome
                        break
                    yield outcome
                    if outcome.block:
                        return
            else:
                if stream is None:
                    yield Output.empty()
                    return
                if isinstance(stream, Output):
                    yield stream
                    if stream.block:
                        return
                    continue
                input = stream
        yield input.get_plain_text()

    def match(
        self, text: str
    ) -> EventQueue[
        Callable[[Input], Input | Output | Generator[Input | Output, Any, None]]
    ]:
        queue = EventQueue()

        for interceptor in self.interceptors:
            if interceptor["router"].match(text):
                queue.push(interceptor["priority"], interceptor["handler"])

        return queue
