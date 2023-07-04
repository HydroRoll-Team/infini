import argparse
from tkinter import messagebox

def main():
    # 创建解析器对象
    parser = argparse.ArgumentParser(description='HydroRoll 命令行工具')

    # 添加命令行参数
    parser.add_argument('--gui', action='store_true', help='显示弹窗')
    parser.add_argument('--path', help='指定路径')

    # 解析命令行参数
    args = parser.parse_args()

    # 处理命令行参数
    if args.gui:
        messagebox.showinfo('提示', '这是一个弹窗！')

    if args.path:
        print('输入的路径:', args.path)

if __name__ == '__main__':
    main()
