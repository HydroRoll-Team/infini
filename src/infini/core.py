from infini.input import Input
from infini.interceptor import Interceptor
from infini.generator import Generator
from infini.handler import Handler
from infini.output import Output


class Core:
    pre_interceptor: Interceptor
    handler: Handler
    generator: Generator
    interceptor: Interceptor

    def input(self, input: Input):
        if isinstance(pre_intercepted_stream := self.pre_intercept(input), Output):
            yield self.generate(pre_intercepted_stream)
            return
        for handled_stream in self.handle(pre_intercepted_stream):
            if handled_stream.is_empty():
                return
            yield self.intercept(self.generate(handled_stream))

    def pre_intercept(self, input: Input) -> Input | Output:
        return self.pre_interceptor.input(input)

    def handle(self, input: Input):
        iterator = self.handler.input(input)
        for output in iterator:
            yield output

    def generate(self, output: Output) -> str:
        return self.generator.output(output)

    def intercept(self, output: str) -> str:
        return (
            self.generate(callback)
            if isinstance(callback := self.interceptor.output(output), Output)
            else callback
        )
