from pathlib import Path
from .utils.cli import parse_args
from .consts import templates
from .logging import logger

import os
import importlib
import sys


def main():
    args = parse_args()

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

        logger.success("HydroRoll 规则包模板已创建！")

    if args.run:
        sys.path.append(str(path))
        importlib.import_module("event")


if __name__ == "__main__":
    main()
