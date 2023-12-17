from pathlib import Path
from .utils.cli import parse_args
from .consts import templates
from .logging import logger
from .register import register

import os
import importlib
import sys


def main():
    args = parse_args()

    if args.gui:
        logger.critical("选项[--gui]尚未被支持！")
        sys.exit(1)

    path = (
        Path(args.path).resolve()
        if hasattr(args, "path")
        else Path(os.getcwd()).resolve()
    )

    if args.operate == "new":
        if path.exists() and not args.force:
            logger.error("指定的文件夹已经存在！")
            sys.exit(1)

        path.mkdir(parents=True, exist_ok=True)
        (path / "handler.py").write_text(templates.HANDLER, encoding="utf-8")
        (path / "event.py").write_text(templates.EVENT, encoding="utf-8")
        (path / "tests.py").write_text(templates.TEST, encoding="utf-8")

        logger.success("HydroRoll 规则包模板已创建！")

    if args.operate == "test":
        exceptions = []

        logger.info(f"开始测试规则包: {path.name}...")
        logger.info("初始化规则包中...")

        try:
            register.regist(path)
        except Exception as error:
            if args.verbose:
                logger.exception(error)
                logger.critical(f"初始化规则包时出现异常： {error}")
            exceptions.append(error)

        try:
            errors = importlib.import_module(f"{path.name}.tests").test()
            exceptions.extend(errors)
        except Exception as error:
            if args.verbose:
                logger.exception(error)
                logger.critical(f"测试规则包时出现异常： {error}")
            exceptions.append(error)

        logger.info(f"测试规则包 {path.name} 出现 {len(exceptions)} 个异常, 测试完成.")


if __name__ == "__main__":
    main()
