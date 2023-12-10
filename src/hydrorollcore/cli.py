from pathlib import Path
from .consts import templates
from .logging import logger

import argparse
import os
import sys
import importlib


class Cli:
    def parse_args(self, argv: list[str] | None = None):
        parser = argparse.ArgumentParser(description="HydroRoll 命令行工具")

        parser.add_argument("--new", action="store_true", help="创建一个 HydroRoll 规则包模板")
        parser.add_argument("--run", action="store_true", help="运行 HydroRoll 规则包")
        parser.add_argument("--gui", action="store_true", help="显示弹窗")
        parser.add_argument("--path", help="指定路径")

        args = parser.parse_args(argv if argv else sys.argv[1:])

        if args.gui:
            logger.critical("选项[--gui]尚未被支持！")
            sys.exit(1)

        path = Path(args.path).resolve() if args.path else Path(os.getcwd()).resolve()
        if args.new and args.run:
            logger.error("无法确定的指令要求: 你同时指定了new与run指令。")
            sys.exit(1)

        if args.new:
            if path.exists():
                logger.error("指定的文件夹已经存在！")
                sys.exit(1)

            path.mkdir(parents=True, exist_ok=True)
            (path / "rule.py").write_text(templates.RULE, encoding="utf-8")
            (path / "event.py").write_text(templates.EVENT, encoding="utf-8")
            (path / "dice.py").write_text(templates.DICE, encoding="utf-8")

            logger.success("HydroRoll 规则包模板已创建！")

        if args.run:
            sys.path.append(str(path))
            importlib.import_module("event")
