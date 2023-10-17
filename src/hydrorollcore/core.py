import importlib
from typing import List
from .exceptions import RuleLoadError
from .rule import Rule


class Core:
    def __init__(self, config):
        self.rule_dir = config.rule_dir
        self.rules = config.rules

    async def load_rules(self) -> List[Rule]:
        loaded_rules = []
        for rule in self.rules:
            try:
                module = importlib.import_module(rule)
            except ImportError as e:
                raise RuleLoadError(f'Failed to load rule {rule}: {e}')
            try:
                rule_cls = getattr(module, rule.split('.')[-1])
                if not issubclass(rule_cls, Rule):
                    raise RuleLoadError(f"Class '{rule_cls.__name__}' is not a subclass of 'Rule'")
            except AttributeError as e:
                raise RuleLoadError(f"Failed to get rule class from module '{rule}': {e}")
            loaded_rules.append(rule_cls())
        return loaded_rules
