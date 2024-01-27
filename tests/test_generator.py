from infini.generator import TextGenerator
from infini.output import Output


def test_generator():
    generator = TextGenerator()
    generator.events = {
        "test.event1": "Event1 文本",
    }
    generator.match(Output("text", "test.event1"))
    assert generator.output(Output("text", "test.event1")) == "Event1 文本"


def test_generator_with_var():
    generator = TextGenerator()
    generator.events = {
        "test.event1": "Event1 文本: {{ var }}",
    }

    assert (
        generator.output(Output("text", "test.event1", variables={"var": "变量测试"}))
        == "Event1 文本: 变量测试"
    )


def test_generator_with_function():
    def add(a, b):
        return a + b

    generator = TextGenerator()
    generator.events = {
        "test.event": "{{ func(1, 2) }}",
    }

    assert (
        generator.output(Output("text", "test.event", variables={"func": add}))
        == "3"
    )
