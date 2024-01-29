from infini.typing import Sequence, Literal


class Router:
    type: Literal["normal"] = "normal"
    signs: set[str]

    def __init__(self, sign: str, alias: Sequence[str] = []) -> None:
        self.signs = {sign}
        self.signs.update(alias)

    def __eq__(self, __router: "Router") -> bool:
        return __router.type == self.type and __router.signs == self.signs

    def match(self, input: str) -> bool:
        return any([input == sign for sign in self.signs])


class Startswith(Router):
    type: Literal["startswith"] = "startswith"

    def match(self, input: str) -> bool:
        input = input.strip()
        return any([input.startswith(sign) for sign in self.signs])


class Contains(Router):
    type: Literal["contains"] = "contains"

    def match(self, input: str) -> bool:
        input = input.strip()
        return any([sign in input for sign in self.signs])


class Endswith(Router):
    type: Literal["endswith"] = "endswith"

    def match(self, input: str) -> bool:
        input = input.strip()
        return any([input.endswith(sign) for sign in self.signs])


class Command(Router):
    type: Literal["command"] = "command"
    prefix: tuple = (".", "/")

    def match(self, input: str) -> bool:
        input = input.strip()
        if input:
            if input.startswith(self.prefix):
                input = input[1:]
                return any([input.startswith(sign) for sign in self.signs])

        return False
