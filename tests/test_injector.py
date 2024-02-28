from infini.injector import Injector


def test_injector():
    def add(a: int, b: int = 0):
        return a + b

    injector = Injector()
    injector.parameters = {"a": 12, "b": 20, "c": 0}
    assert injector.inject(add)() == 32
    assert injector.output(add) == 32
