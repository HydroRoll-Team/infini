from pydantic import BaseModel
from typing import (
    Dict as Dict,
    TYPE_CHECKING as TYPE_CHECKING,
    TypeVar as TypeVar,
    Callable as Callable,
    NoReturn as NoReturn,
    Awaitable as Awaitable,
)


class Config(BaseModel):
    rule_dir: list = []
    rules: list = []


class DiceConfig(BaseModel):
    sides: int
    counts: int
    init_dice_pool: int


class PlayerCard(BaseModel):
    name: str
    traits: list


class Bonus(BaseModel):
    level: int
    cost: int


class WikiPage(BaseModel):
    title: str
    content: str
    tags: list = []


class WikiModel:
    class Setting(BaseModel):
        desc: str
