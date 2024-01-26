from infini.handler import Handler
from infini.input import Input
from infini.output import Output
from infini.router import StartswithRouter


def test_handler():
    input = Input(".add 1 2")

    def add(input: Input) -> Output:
        a, b = map(int, input.get_plain_text().lstrip(".add").split())
        output = Output()
        output.block = False
        output.status = 0
        output.type = "text"
        output.name = str(a + b)
        return output

    def cmd(_: Input) -> Output:
        output = Output()
        output.block = False
        output.status = 0
        output.type = "text"
        output.name = "cmd"
        return output

    handler = Handler()
    handler.handlers = [
        {
            "priority": 2,
            "router": StartswithRouter(".add"),
            "handler": add,
        },
        {
            "priority": 1,
            "router": StartswithRouter("."),
            "handler": cmd,
        },
    ]

    names = []
    for output in handler.input(input):
        names.append(output.name)
    assert names == ["cmd", "3"]


def test_handler_block():
    input = Input(".add 1 2")

    def add(input: Input) -> Output:
        a, b = map(int, input.get_plain_text().lstrip(".add").split())
        output = Output()
        output.block = False
        output.status = 0
        output.type = "text"
        output.name = str(a + b)
        return output

    def cmd(_: Input) -> Output:
        output = Output()
        output.block = True
        output.status = 0
        output.type = "text"
        output.name = "cmd"
        return output

    handler = Handler()
    handler.handlers = [
        {
            "priority": 2,
            "router": StartswithRouter(".add"),
            "handler": add,
        },
        {
            "priority": 1,
            "router": StartswithRouter("."),
            "handler": cmd,
        },
    ]

    names = []
    for output in handler.input(input):
        names.append(output.name)
    assert names == ["cmd"]
