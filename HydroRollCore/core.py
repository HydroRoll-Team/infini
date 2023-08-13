"""HydroRollCore 核心程序"""

import asyncio
from collections import defaultdict
import sys

from typing import Any, List, Optional, Type, Dict

from HydroRollCore.config import MainConfig
from HydroRollCore.rule import Rule, RuleLoadType

__all__ = ['Core']

class Core:
    """HydroRollCore 核心对象，定义了核心的基本方法。
        读取并储存配置 `Config`，加载规则包 `Rule`，并进行事件分发。

    Attributes:
        config: 核心配置。
        should_exit: 核心是否应该进入准备退出状态。
        rules: 当前已经加载的规则包的列表。
        rules_priority_dict: 规则包优先级字典。
        rule_state: 规则包状态。
        global_state: 全局状态。
    """

    config: MainConfig
    should_exit: asyncio.Event
    rules: List[Rule]
    rules_priority_dict: Dict[int, List[Type[Rule]]]
    rule_state: Dict[str, Any]
    global_state: Dict[Any, Any]
    
    def __init__(
        self,
        *,
        config_file: Optional[str] = "config.toml",
        config_dict: Optional[Dict] = None,
        hot_reload: bool = False,
    ):
        """初始化 iamai ，读取配置文件，创建配置，加载规则包。

        Args:
            config_file: 配置文件，如不指定则使用默认的 `config.toml`。
                若指定为 None，则不加载配置文件。
            config_dict: 配置字典，默认为 None。
                若指定字典，则会忽略 config_file 配置，不再读取配置文件。
            hot_reload: 热重载。
                启用后将自动检查 `rule_dir` 中的规则包文件更新，并在更新时自动重新加载。
        """
        self.config = MainConfig()  # type: ignore[assignment]
        self.plugins_priority_dict = defaultdict(list)
        self.plugin_state = defaultdict(type(None))  # type: ignore[assignment]
        self.global_state = {}

        self.adapters = []
        self._restart_flag = False
        self._module_path_finder = ModulePathFinder()
        self._raw_config_dict = {}

        self._config_file = config_file
        self._config_dict = config_dict
        self._hot_reload = hot_reload

        self._extend_plugins = []
        self._extend_plugin_dirs = []
        self._extend_adapters = []
        self._bot_run_hooks = []
        self._bot_exit_hooks = []
        self._adapter_startup_hooks = []
        self._adapter_run_hooks = []
        self._adapter_shutdown_hooks = []
        self._event_preprocessor_hooks = []
        self._event_postprocessor_hooks = []

        sys.meta_path.insert(0, self._module_path_finder)