# Initialized `__init__.py` generated by ipm.
# Documents at https://ipm.hydroroll.team/

from infini.register import Register
from infini.router import Startswith
from infini.input import Input
from infini.output import Output
from .dicer import Dicer

import re

register = Register()
register.regist_textevent(
    "ndice.roll",
    "[{{ username }}]掷骰: "
    "{% if descs|length == 1 %}"
    "{{ descs[0] }}"
    "{% else %}"
    "{{ db }}=[...]="
    "{% for outcome in outcomes %}"
    "{{ outcome }}"
    "{% if not loop.last %}, {% endif %}"
    "{% endfor %}"
    "{% endif %}",
)
register.regist_textevent(
    "ndice.error.bad_roll_string", "[{{ username }}]掷骰时出现异常, 疑似掷骰表达式错误."
)
register.regist_textevent("ndice.error.too_much_round", "[{{ username }}]给入的掷骰轮数超出预期.")
register.regist_textevent(
    "ndice.error.unknown",
    "未知错误: {{ error }}, 可能是掷骰语法异常.\nBUG提交: https://gitee.com/unvisitor/issues",
)
register.regist_textevent("ndice.error.bad_round", "多轮检定的轮数应当是整型数.")
register.regist_textevent("ndice.error.too_much_round", "多轮检定的轮数超出预期.")


def translate_punctuation(string: str) -> str:
    punctuation_mapping = {
        "，": ",",
        "。": ".",
        "！": "!",
        "？": "?",
        "；": ";",
        "：": ":",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "《": "<",
        "》": ">",
    }
    for ch_punct, en_punct in punctuation_mapping.items():
        string = string.replace(ch_punct, en_punct)
    return string


def format_str(message: str, begin=None, lower=True) -> str:
    regex = r"[<\[](.*?)[\]>]"
    message = str(message).lower() if lower else str(message)
    msg = translate_punctuation(
        re.sub("\s+", " ", re.sub(regex, "", message)).strip(" ")
    )
    if msg.startswith("/"):
        msg = "." + msg[1:]

    if begin:
        if isinstance(begin, str):
            begin = [
                begin,
            ]
        elif isinstance(begin, tuple):
            begin = list(begin)

        begin.sort(reverse=True)
        for b in begin:
            msg = msg.replace(b, "").lstrip(" ")

    return msg


def roll(_: Input, args: str, name: str = None) -> str:
    time = 1
    if "#" in args:
        args = args.split("#")

        try:
            time = int(args[0].strip())
            if time > 20:
                return Output(
                    "text", "ndice.error.too_much_round", variables={"username": name}
                )
        except ValueError:
            return Output("text", "ndice.error.bad_round", variables={"username": name})

        if len(args) == 1:
            args = "1d100"
        else:
            args = args[1]
    else:
        args = args.strip()

    args = args.split()
    if len(args) > 1:
        reason = args[1]
    else:
        reason = None

    roll_string = args[0]
    descs = []
    outcomes = []

    try:
        dice = Dicer(roll_string).roll()
        descs.append(dice.description())
        outcomes.append(dice.outcome)

        for _ in range(time - 1):
            dice.roll()
            descs.append(dice.description())
            outcomes.append(dice.outcome)
    except ValueError:
        return Output(
            "text",
            "ndice.error.bad_roll_string",
            status=1,
            variables={"username": name},
        )

    return Output(
        "text",
        "ndice.roll",
        variables={
            "username": name,
            "descs": descs,
            "outcomes": outcomes,
            "db": dice.db,
        },
    )


@register.handler(router=Startswith(".r"), priority=0)
def roll_handler(input: Input):
    args = format_str(input.get_plain_text(), begin=(".r", ".roll"))
    name = input.variables.get("nickname") or "苏向夜"
    if not args:
        return roll(input, "1d100", name=name)

    try:
        return roll(input, args, name=name)
    except Exception as error:
        return Output("text", "ndice.error.unknown", variables={"error": str(error)})
