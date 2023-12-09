from pathlib import Path
from .consts import templates

# from tkinter import messagebox

import argparse
import os
import sys


class Cli:
    def parse_args(self):
        parser = argparse.ArgumentParser(description="HydroRoll 命令行工具")

        parser.add_argument("--new", action="store_true", help="创建一个 HydroRoll 规则包模板")
        parser.add_argument("--run", action="store_true", help="运行 HydroRoll 规则包")
        # parser.add_argument("--gui", action="store_true", help="显示弹窗")
        parser.add_argument("--path", help="指定路径")

        args = parser.parse_args()

        # if args.gui:
        #     messagebox.showinfo("提示", "这是一个弹窗！")

        if not args.path:
            path = Path(os.getcwd()).resolve()
        else:
            path = Path(args.path).resolve()

        if args.new and args.run:
            print("无法确定的指令要求: 你同时指定了new与run指令。")
            sys.exit(1)

        if args.new:
            if path.exists():
                print("指定的文件夹已经存在！")
                sys.exit(1)

            path.mkdir(parents=True, exist_ok=True)
            (path / "rule.py").write_text(templates.RULE)
            (path / "event.py").write_text(templates.EVENT)
            (path / "dice.py").write_text(templates.DICE)

            print("HydroRoll 规则包模板已创建！")
