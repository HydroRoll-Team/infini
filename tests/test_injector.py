from infini.injector import Injector


def test_injector():
    def name(name: str):
        return name

    def add(a: int, b: int = 0):
        return a + b

    injector = Injector()
    injector.parameters = {"a": 12, "b": 20, "c": 0, "card_name": name}
    assert injector.inject(add)() == 32
    assert injector.output(add) == 32
