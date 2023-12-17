from infini import Handler, MessageEvent
from infini.matcher import MatcherEvent
from infini.event import InfiniEvent
from .event import MyEvent


class MyHandler(Handler):
    """自设业务函数"""

    priority: int = 0  # 业务函数权重

    def process(self, event: MatcherEvent) -> InfiniEvent:
        """声明规则包检定方式"""
        plain_text = event.get_plain_text()
        return MyEvent("rule.example_event", plain_text=plain_text)

