import importlib
from typing import List
from .exceptions import RuleLoadError
from .rule import Rule
from .config import Config


class Core:
    def __init__(self, config: Config):
        self.rule_dir = config.rule_dir
        self.rules = config.rules

    def load_rules(self) -> List[Rule]:
        loaded_rules = []
        for rule in self.rules:
            try:
                module = importlib.import_module(rule)
            except ImportError as e:
                raise RuleLoadError(f"Failed to load rule {rule}: {e}") from e
            try:
                rule_cls = getattr(module, rule.split(".")[-1])
                if not issubclass(rule_cls, Rule):
                    raise RuleLoadError(
                        f"Class '{rule_cls.__name__}' is not a subclass of 'Rule'"
                    )
            except AttributeError as e:
                raise RuleLoadError(
                    f"Failed to get rule class from module '{rule}': {e}"
                ) from e
            loaded_rules.append(rule_cls())
        return loaded_rules
