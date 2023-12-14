import argparse
import sys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="Infini CLI", description="Infini 命令行工具")

    parser.add_argument("--new", action="store_true", help="创建一个 Infini 规则包模板")
    parser.add_argument("--load", action="store_true", help="导入 Infini 规则包")
    parser.add_argument("--test", action="store_true", help="运行 Infini 规则包测试")
    parser.add_argument("--gui", action="store_true", help="显示弹窗")
    parser.add_argument("--path", help="指定路径")

    args = parser.parse_args(argv if argv else sys.argv[1:])
    return args
