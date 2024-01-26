from infini.output import Output
from infini.typing import Dict, Callable


class Generator:
    events: Dict[str, str]
    global_variables: Dict[str, str | Callable]

    def output(self, output: Output) -> str:
        return output.name
