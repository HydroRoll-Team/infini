"""
infini 终端命令解析模块
"""

import argparse
import sys


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    # sourcery skip: extract-duplicate-method
    parser = argparse.ArgumentParser(prog="Infini CLI", description="Infini 命令行工具")

    parser.add_argument("--gui", action="store_true", help="启用 GUI 模式")

    subparsers = parser.add_subparsers(title="功能件", dest="operate")

    # 子命令 `new`
    new_parser = subparsers.add_parser("new", help="创建一个 Infini 规则包模板")
    new_parser.add_argument("path", help="目标位置")
    new_parser.add_argument("-v", "--verbose", action="store_true", help="异常追踪")
    new_parser.add_argument("-f", "--force", action="store_true", help="强制创建")

    # 子命令 `test`
    test_parser = subparsers.add_parser("test", help="测试 Infini 规则包")
    test_parser.add_argument("path", help="目标位置")
    test_parser.add_argument("-v", "--verbose", action="store_true", help="异常追踪")

    return parser.parse_args(argv or sys.argv[1:])
