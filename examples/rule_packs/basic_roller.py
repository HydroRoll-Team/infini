import random
import re


def get_help():
    """返回此规则包的帮助信息"""
    return """
--- 基础掷骰 (Basic Roller) ---
.r <表达式> : 执行一个掷骰表达式。
  示例: .r 2d6
        .r d100+10
        .r 1d20-2
"""


def handle_command(command):
    """处理基础掷骰指令"""
    # 我们规定基础指令以 .r 开头
    if not command.lower().startswith(".r "):
        return None  # 不是我的指令，我不处理

    expression = command[3:].strip()  # 获取 .r 后面的内容

    # 清理表达式中的空格
    expression = expression.lower().replace(" ", "")

    # 正则表达式来匹配 XdY+/-Z
    match = re.match(r"(\d*)d(\d+)([+-]\d+)?", expression)
    if not match:
        return f"基础掷骰格式错误: {expression}"

    num_dice_str, num_sides_str, modifier_str = match.groups()

    num_dice = int(num_dice_str) if num_dice_str else 1
    num_sides = int(num_sides_str)
    modifier = int(modifier_str) if modifier_str else 0

    if num_dice <= 0 or num_sides <= 0:
        return "骰子数量和面数必须大于0。"

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    base_total = sum(rolls)
    final_total = base_total + modifier

    roll_details = f"({'+'.join(map(str, rolls))})"
    if modifier != 0:
        return f"掷骰: {expression} -> {final_total} [{roll_details}{modifier:+}]"
    else:
        return f"掷骰: {expression} -> {final_total} {roll_details}"
