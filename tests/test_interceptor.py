from infini.input import Input
from infini.interceptor import Interceptor
from infini.output import Output
from infini.router import ContainsRouter


def test_interceptor():
    input = Input("这个人叫简律纯.")
    valid_input = Input("这个叫苏向夜.")

    def intercept(_: Input) -> Input | Output:
        return Output("text", "block.jianlvchun", block=True)  # TODO 拦截器阻塞标识

    interceptor = Interceptor()
    interceptor.interceptors = [
        {
            "priority": 1,
            "router": ContainsRouter("简律纯"),
            "handler": intercept,
        }
    ]
    output = interceptor.input(input)
    assert isinstance(output, Output)
    assert output.name == "block.jianlvchun"

    valid_output = interceptor.input(valid_input)
    assert isinstance(valid_output, Input)
    assert valid_output.get_plain_text() == "这个叫苏向夜."
