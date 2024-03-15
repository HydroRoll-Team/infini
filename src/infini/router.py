from infini.typing import Sequence, Literal
from infini.input import Input


class Router:
    type: Literal["text"] = "text"
    signs: set[str]

    def __init__(self, sign: str, alias: Sequence[str] = []) -> None:
        self.signs = {sign}
        self.signs.update(alias)

    def __eq__(self, __router: "Router") -> bool:
        return __router.type == self.type and __router.signs == self.signs

    def match(self, plain_text: str) -> bool:
        text = plain_text.strip()
        return any([text == sign for sign in self.signs])


class Startswith(Router):
    name: Literal["startswith"] = "startswith"

    def match(self, plain_text: str) -> bool:
        text = plain_text.strip()
        return any([text.startswith(sign) for sign in self.signs])


class Contains(Router):
    name: Literal["contains"] = "contains"

    def match(self, plain_text: str) -> bool:
        return any([sign in plain_text for sign in self.signs])


class Endswith(Router):
    name: Literal["endswith"] = "endswith"

    def match(self, input: Input) -> bool:
        text = input.get_plain_text().strip()
        return any([text.endswith(sign) for sign in self.signs])


class Command(Router):
    name: Literal["command"] = "command"
    prefix: tuple = (".", "/", "。", "!", "！")

    def match(self, input: Input) -> bool:
        text = input.get_plain_text().strip()
        if text.startswith(self.prefix):
            text = text[1:]
            return any([text.startswith(sign) for sign in self.signs])

        return False
