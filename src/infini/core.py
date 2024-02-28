from infini.input import Input
from infini.interceptor import Interceptor
from infini.generator import TextGenerator
from infini.handler import Handler
from infini.injector import Injector
from infini.output import Output
from infini.typing import Any, Generator, Union
from infini.exceptions import ValueError


class Core:
    pre_interceptor: Interceptor
    handler: Handler
    generator: TextGenerator
    interceptor: Interceptor
    injector: Injector

    def input(
        self, input: Input
    ) -> Generator[Union[str, Output], Any, None]:  # TODO 支持Workflow
        for pre_intercepted_stream in self.pre_intercept(input):
            if isinstance(pre_intercepted_stream, Output):
                if not isinstance(pre_intercepted_stream, Output):
                    raise ValueError(
                        "Interceptor functions should return or yield a `Output` object."
                    )
                if pre_intercepted_stream.is_empty():
                    return
                yield self.generate(pre_intercepted_stream)
                if pre_intercepted_stream.block:
                    return
            else:
                input = pre_intercepted_stream

        for handled_stream in self.handle(input):
            if not isinstance(handled_stream, Output):
                raise ValueError(
                    "Handler functions should return or yield a `Output` object."
                )
            if handled_stream.is_empty():
                return
            outcome = self.generate(handled_stream)
            for stream in self.intercept(outcome):
                if isinstance(stream, Output):
                    if stream.is_empty():
                        return
                    yield self.generate(stream)
                    if stream.block:
                        return
                    continue
                outcome = stream
            yield outcome
            if handled_stream.block:
                return

    def pre_intercept(self, input: Input) -> Generator[Union[Input, Output], Any, None]:
        return self.pre_interceptor.input(input)

    def handle(self, input: Input) -> Generator[Output, Any, None]:
        iterator = self.handler.input(input)
        for output in iterator:
            yield output

    def generate(self, output: Output) -> str:
        return self.generator.output(output, self.injector)

    def intercept(self, output_text: str) -> Generator[Union[str, Output], Any, None]:
        return self.interceptor.output(output_text)
