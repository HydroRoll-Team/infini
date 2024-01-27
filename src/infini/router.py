from infini.typing import Sequence, List


class Router:
    signs: List[str]

    def __init__(self, sign: str, alias: Sequence[str] = []) -> None:
        self.signs = [sign]
        self.signs.extend(alias)

    def match(self, input: str) -> bool:
        return any([input == sign for sign in self.signs])


class Startswith(Router):
    def match(self, input: str) -> bool:
        input = input.strip()
        return any([input.startswith(sign) for sign in self.signs])


class Contains(Router):
    def match(self, input: str) -> bool:
        input = input.strip()
        return any([sign in input for sign in self.signs])


class Endswith(Router):
    def match(self, input: str) -> bool:
        input = input.strip()
        return any([input.endswith(sign) for sign in self.signs])
