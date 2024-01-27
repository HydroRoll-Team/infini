from infini.output import Output
from infini.typing import Dict, Callable
from infini.exceptions import UnknownEvent
from jinja2 import Template


class TextGenerator:  # TODO 兼容多类型事件
    events: Dict[str, str]
    global_variables: Dict[str, str | Callable]

    def __init__(self) -> None:
        self.events = {}
        self.global_variables = {}

    def output(self, output: Output) -> str:
        assert output.type != "workflow", "Workflow 事件无法产出文本"
        variables = self.global_variables.copy()
        variables.update(output.variables)
        return self.match(output).render(variables)

    def match(self, output: Output) -> Template:
        if context := self.events.get(output.name):
            return Template(context)
        raise UnknownEvent(f"事件不存在: {output.name}")
