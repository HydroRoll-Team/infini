from infini.handler import Handler
from infini.input import Input
from infini.output import Output
from infini.router import StartswithRouter


def test_handler():
    input = Input(".add 1 2")

    def add(input: Input) -> Output:
        return Output(
            "text",
            str(sum(list(map(int, input.get_plain_text().lstrip(".add").split())))),
            status=0,
            block=False,
        )

    def cmd(_: Input) -> Output:
        return Output("text", "cmd", status=0, block=False)

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
        return Output(
            "text",
            str(sum(list(map(int, input.get_plain_text().lstrip(".add").split())))),
            status=0,
            block=False,
        )

    def cmd(_: Input) -> Output:
        return Output("text", "cmd", status=0, block=True)

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


def test_handler_interator():
    input = Input(".add 1 2")

    def add(input: Input):
        yield Output(
            "text",
            str(sum(list(map(int, input.get_plain_text().lstrip(".add").split())))),
            status=0,
            block=False,
        )
        yield Output("text", "ok", status=0, block=False)

    handler = Handler()
    handler.handlers = [
        {
            "priority": 1,
            "router": StartswithRouter(".add"),
            "handler": add,
        },
    ]

    names = []
    for output in handler.input(input):
        names.append(output.name)
    assert names == ["3", "ok"]
