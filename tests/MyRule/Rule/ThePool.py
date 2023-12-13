from infini import Rule
from .wiki import Wiki


class Config:
    __config_name__ = "ThePool"


class ThePool(Rule):
    config: Config
    wiki: Wiki

    class DefaultDice:
        _sides = 6
        _counts = 1
        _init_dice_pool = 15

    class Bonus:
        """奖励骰

        要分配奖励，你需要花费起始骰池中的骰子。消耗的数量等于奖励骰的数量乘以它自身。
        """

    class PlayerCard:
        """角色卡"""

        def Trait(self):
            """特质标准判断"""
            return self.__str__() if self.__str__() != "" else None
