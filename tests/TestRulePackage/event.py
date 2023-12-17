from infini import MessageEvent


class MyEvent(MessageEvent):
    """自定义消息事件"""
    name = "example_event"
    output = "捕获到输入: {plain_text}"
