import random
import re


def get_help():
    """返回此规则包的帮助信息"""
    return """
--- 克苏鲁的呼唤 (Call of Cthulhu) ---
.ra <技能值> : 对指定的技能值进行成功/失败检定。
  示例: .ra 75
"""


def handle_command(command):
    """处理COC检定指令"""
    command = command.lower().strip()

    # 我们规定COC检定指令以 .ra 开头
    match = re.match(r"^\.ra\s*(\d+)$", command)
    if not match:
        return None  # 不是我的指令，我不处理

    skill_value = int(match.group(1))
    roll = random.randint(1, 100)

    # 判断结果
    if roll <= 1:
        result_text = "大成功 (Critical Success)"
    elif roll > 95:  # COC 7版规则大失败
        result_text = "大失败 (Fumble)"
    elif roll <= skill_value / 5:
        result_text = "极难成功 (Extreme Success)"
    elif roll <= skill_value / 2:
        result_text = "困难成功 (Hard Success)"
    elif roll <= skill_value:
        result_text = "成功 (Regular Success)"
    else:
        result_text = "失败 (Failure)"

    return f"COC检定 (目标: {skill_value}) -> 掷骰: {roll} -> {result_text}"
