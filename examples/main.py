# main.py
import os
import importlib

# --- 配置区 ---
# 在这里指定你想要加载的规则包文件名 (不含 .py)
# 你可以随时修改这个列表来开启或关闭不同的规则包
ENABLED_RULE_PACKS = [
    "basic_roller",
    "coc",
]


class DiceBotCore:
    def __init__(self, rule_pack_names):
        self.loaded_packs = []
        self.load_rule_packs(rule_pack_names)

    def load_rule_packs(self, rule_pack_names):
        """动态加载指定的规则包"""
        print("正在加载规则包...")
        for name in rule_pack_names:
            try:
                # 动态导入模块
                module = importlib.import_module(f"rule_packs.{name}")
                # 检查模块是否符合我们的结构要求
                if hasattr(module, "handle_command"):
                    self.loaded_packs.append(module)
                    print(f"  - 规则包 '{name}' 加载成功。")
                else:
                    print(
                        f"  - 警告: 规则包 '{name}'缺少 'handle_command' 函数，已跳过。"
                    )
            except ImportError:
                print(f"  - 错误: 找不到名为 '{name}' 的规则包。")
        print("-" * 20)

    def process_command(self, command):
        """将指令传递给所有加载的规则包"""
        for pack in self.loaded_packs:
            result = pack.handle_command(command)
            if result is not None:
                return result  # 一旦有规则包处理了指令，就立即返回结果
        return "无法识别的指令。输入 'help' 查看可用指令。"

    def get_all_help(self):
        """收集所有已加载规则包的帮助信息"""
        help_texts = ["--- 欢迎使用模块化骰子机器人 ---"]
        for pack in self.loaded_packs:
            if hasattr(pack, "get_help"):
                help_texts.append(pack.get_help())
        return "\n".join(help_texts)


def main():
    """程序主循环"""
    bot = DiceBotCore(ENABLED_RULE_PACKS)

    print("机器人已启动。输入 'exit' 退出。")
    print(bot.get_all_help())  # 启动时显示帮助信息

    while True:
        user_input = input("\n> ")

        if user_input.lower() == "exit":
            print("感谢使用，再见！")
            break
        elif user_input.lower() == "help":
            print(bot.get_all_help())
            continue

        result = bot.process_command(user_input)
        print(result)


if __name__ == "__main__":
    main()
