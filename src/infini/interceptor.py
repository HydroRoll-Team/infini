from infini.input import Input
from infini.output import Output
from infini.typing import List, RouterType, Callable
from infini.queue import EventQueue


class Interceptor:
    interceptors: List[RouterType]

    def input(self, input: Input) -> Input | Output:
        queue = self.match(input.get_plain_text())
        while not queue.is_empty():
            if isinstance(intercepted := queue.pop()(input), Output):
                return intercepted  # TODO 允许拦截器产出文本
            else:
                input = intercepted
        return input

    def output(self, output_text: str) -> str | Output:
        queue = self.match(output_text)  # TODO 需要测试输出拦截情况
        input = Input(output_text)
        while not queue.is_empty():
            if isinstance(intercepted := queue.pop()(input), Output):
                return intercepted
            else:
                input = intercepted
        return output_text

    def match(self, text: str) -> EventQueue[Callable[[Input], Input | Output]]:
        queue = EventQueue()

        for interceptor in self.interceptors:
            if interceptor["router"].match(text):
                queue.push(interceptor["priority"], interceptor["handler"])

        return queue
