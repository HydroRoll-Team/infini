RULE = """from infini import Rule, Result, Dice


class MyRule(Rule):
    \"\"\"自设规则包\"\"\"

    name = "MyRule"
    priority: int = 0

    def __init__(self) -> None:
        \"\"\"初始化你的规则包\"\"\"

    def check(self, dice: Dice) -> Result:
        \"\"\"声明规则包检定方式\"\"\"
        return Result("myevent.event1", True)
"""

EVENT = """from infini import Event

__events__ = ["MyEvent"]


class MyEvent(Event):
    name = "event1"
    output = "检定成功!"
"""

DICE = """from infini import Dice

import random
import re


class BaseDice(Dice):
    \"\"\"多面骰\"\"\"

    def __init__(self, roll_string: str = "") -> None:
        self.roll_string = roll_string
        self.parse()

    def parse(self) -> "Dice":
        self.dices = []
        split = re.split(r"[dD]", self.roll_string)

        if split[0]:
            self.a = int(split[0])
        else:
            self.a = 1

        if split[1]:
            self.b = int(split[1])
        else:
            self.b = 100

        self.db = f"{self.a}D{self.b}"
        self.dices += [f"D{self.b}"] * self.a
        return self

    def roll(self) -> int:
        self.results = []

        for _ in range(self.a):
            result = random.randint(1, self.b)

            self.results.append(result)

        self.outcome = sum(self.results)
        return self.outcome
"""
