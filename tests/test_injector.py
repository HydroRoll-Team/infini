from infini.handler import Handler
from infini.injector import Injector
from infini.input import Input
from infini.loader import Loader
from infini.output import Output
from infini.router import Startswith


def test_injector():
    def name(name: str):
        return name

    def add(a: int, b: int = 0):
        return a + b

    injector = Injector()
    injector.parameters = {"a": 12, "b": 20, "c": 0, "card_name": name}
    assert injector.inject(add)() == 32
    assert injector.output(add) == 32


def test_handler_injector():
    input = Input("test_message")

    def absolute(input: Input[str], plain_text: str) -> Output:
        return input.output(
            "text",
            "absolute",
            block=False,
            variables={
                "text": plain_text,
            },
        )

    handler = Handler()
    handler.handlers = [
        {
            "priority": 2,
            "router": Startswith(""),
            "handler": absolute,
        },
    ]

    core = Loader().into_core()
    core.handler = handler
    core.generator.events = {
        "absolute": "{{ text }}",
    }

    for output in core.input(input):
        assert output == "test_message"
