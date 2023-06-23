import os
import importlib.util

__all__ = ["Rule"]

class Rule:
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def load_modules(self):
        # 获取指定文件夹下的所有文件和文件夹
        file_list = os.listdir(self.folder_path)
        module_list = []

        # 遍历文件列表
        for file_name in file_list:
            file_path = os.path.join(self.folder_path, file_name)

            # 判断是否为Python文件或者包
            if file_name.startswith('_') or not file_name.endswith(".py"):
                continue

            # 尝试加载模块
            module_name = os.path.splitext(file_name)[0]
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            module_list.append(module)

        return module_list
