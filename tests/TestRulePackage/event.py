from infini import MessageEvent

__events__ = ["MyEvent"]


class MyEvent(MessageEvent):
    name = "event1"
    output = "检定成功!"
