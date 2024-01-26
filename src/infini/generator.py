from infini.output import Output
from infini.typing import Dict, Callable
from infini.exceptions import UnknownEvent
from jinja2 import Template


class Generator:
    events: Dict[str, str]
    global_variables: Dict[str, str | Callable]

    def output(self, output: Output) -> str:
        assert output.type != "workflow", "Workflow 事件无法产出文本"
        template = self.match(output)
        return template.render(output.variables)

    def match(self, output: Output) -> Template:
        if context := self.events.get(output.name):
            return Template(context)
        raise UnknownEvent(f"事件不存在: {output.name}")
