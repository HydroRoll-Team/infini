RULE = """from infini import Handler, Result


class HandlerRule(Handler):
    \"\"\"自设规则包\"\"\"

    name = "MyRule"
    priority: int = 0

    def __init__(self) -> None:
        \"\"\"初始化你的规则包\"\"\"

    def process(self) -> Result:
        \"\"\"声明规则包检定方式\"\"\"
        return Result("event1", True)
"""

EVENT = """from infini import MessageEvent

__events__ = ["MyEvent"]


class MyEvent(MessageEvent):
    name = "event1"
    output = "检定成功!"
"""

TEST = """from infini.matcher import matcher, MatcherEvent

def test():
    event = MatcherEvent("event1")
    print(matcher.run(event))
"""
