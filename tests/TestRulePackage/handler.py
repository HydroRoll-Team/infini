from infini import Handler, Result

__handlers__ = ["HandlerRule"]


class HandlerRule(Handler):
    """自设业务函数"""

    name = "MyRule" # 规则包名
    priority: int = 0 # 规则包权重

    def process(self, **kwargs) -> Result:
        """声明规则包检定方式"""
        return Result("event1", True)
