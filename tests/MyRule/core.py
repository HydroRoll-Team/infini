import os
import importlib
from typing import List
from pydantic import BaseModel
import asyncio

class Rule(BaseModel):
    name: str
    config_name: str

    async def success(self):
        # 处理成功事件的逻辑
        pass

    async def fail(self):
        # 处理失败事件的逻辑
        pass

async def load_rules_from_folder(folder_path: str) -> List[Rule]:
    rules = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".py"):
            module_name = file_name[:-3]
            module = importlib.import_module(module_name)
            for name, obj in module.__dict__.items():
                if isinstance(obj, type) and issubclass(obj, Rule) and obj != Rule:
                    rules.append(obj())
    return rules

async def process_event(rules: List[Rule], event: str):
    tasks = []
    for rule in rules:
        if hasattr(rule, event):
            task = getattr(rule, event)()
            tasks.append(task)
    await asyncio.gather(*tasks)

async def main():
    folder_path = "tests/MyRule/Rule"
    rules = await load_rules_from_folder(folder_path)
    await process_event(rules, "success")

asyncio.run(main())
