from infini.generator import Generator
from infini.output import Output


def test_generator():
    generator = Generator()
    generator.events = {
        "test.event1": "Event1 文本",
    }
    generator.match(Output("text", "test.event1"))
    assert generator.output(Output("text", "test.event1")) == "Event1 文本"
