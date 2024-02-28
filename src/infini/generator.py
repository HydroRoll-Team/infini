from infini.output import Output
from infini.typing import Dict, Callable, Union
from infini.exceptions import UnknownEvent
from infini.injector import Injector
from jinja2 import Template


class TextGenerator:  # TODO 兼容多类型事件
    events: Dict[str, str]
    global_variables: Dict[str, Union[str, Callable]]

    def __init__(self) -> None:
        self.events = {}
        self.global_variables = {}

    def output(self, output: Output, injector: Injector) -> str:
        assert output.type == "text", "文本生成器应当传入类型为 'text' 的 Output 实例"
        variables = self.global_variables.copy()
        variables.update(output.variables)
        for name, variable in variables.items():
            if callable(variable):
                variables[name] = injector.output(variable, output.variables)
        return self.match(output).render(variables)

    def match(self, output: Output) -> Template:
        if context := self.events.get(output.name):
            return Template(context)
        raise UnknownEvent(f"事件不存在: {output.name}")
