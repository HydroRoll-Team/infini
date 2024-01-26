class Router:
    sign: str

    def __init__(self, sign: str) -> None:
        self.sign = sign

    def match(self, input: str) -> bool:
        return self.sign == input.strip()


class StartswithRouter(Router):
    def match(self, input: str) -> bool:
        return input.strip().startswith(self.sign)


class ContainsRouter(Router):
    def match(self, input: str) -> bool:
        return self.sign in input.strip()


class Endswith(Router):
    def match(self, input: str) -> bool:
        return input.strip().endswith(self.sign)
