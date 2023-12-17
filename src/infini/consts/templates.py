HANDLER = """from infini import Handler, MessageEvent
from infini.matcher import MatcherEvent
from .event import MyEvent


class MyHandler(Handler):
    \"\"\"自设业务函数\"\"\"

    name = "example_handler"  # 业务函数事件名
    priority: int = 0  # 业务函数权重

    def process(self, event: MatcherEvent) -> MessageEvent:
        \"\"\"声明规则包检定方式\"\"\"
        plain_text = event.get_plain_text()
        return MyEvent("rule.example_event", plain_text=plain_text)

"""

EVENT = """from infini import MessageEvent


class MyEvent(MessageEvent):
    \"\"\"自定义消息事件\"\"\"
    name = "example_event"
    output = "捕获到输入: {plain_text}"
"""

TEST = """from infini.matcher import matcher, MatcherEvent


def test():
    event = MatcherEvent("rule.example_handler", string="测试")
    try:
        result = matcher.run(event)
        assert result == "捕获到输入: 测试"
    except Exception as error:
        return error
    return []

"""
