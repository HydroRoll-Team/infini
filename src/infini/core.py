from infini.input import Input
from infini.interceptor import Interceptor
from infini.generator import TextGenerator
from infini.handler import Handler
from infini.output import Output
from infini.typing import Any, Generator


class Core:
    pre_interceptor: Interceptor
    handler: Handler
    generator: TextGenerator
    interceptor: Interceptor

    def input(self, input: Input) -> Generator[str, Any, None]:
        for pre_intercepted_stream in self.pre_intercept(input):
            if isinstance(pre_intercepted_stream, Output):
                yield self.generate(pre_intercepted_stream)
                if pre_intercepted_stream.block or pre_intercepted_stream.is_empty():
                    return
            else:
                input = pre_intercepted_stream

        for handled_stream in self.handle(input):
            if handled_stream.is_empty():
                return
            outcome = self.generate(handled_stream)
            for stream in self.intercept(outcome):
                if isinstance(stream, Output):
                    yield self.generate(stream)
                    continue
                outcome = stream
            if handled_stream.block:
                return
            yield outcome

    def pre_intercept(self, input: Input) -> Generator[Output | Input, Any, None]:
        return self.pre_interceptor.input(input)

    def handle(self, input: Input):
        iterator = self.handler.input(input)
        for output in iterator:
            yield output

    def generate(self, output: Output) -> str:
        return self.generator.output(output)

    def intercept(self, output_text: str) -> Generator[Output | str, Any, None]:
        return self.interceptor.output(output_text)
