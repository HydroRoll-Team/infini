from infini.typing import List, ModuleType
from infini.const import SRC_HOME

import importlib
import sys


def require(name: str, paths: List | None = None) -> ModuleType:
    paths = [
        str(path)
        for path in (
            (list(paths) + [str(SRC_HOME / name)]) if paths else [str(SRC_HOME / name)]
        )
    ]
    sys.path.extend(paths)
    module = importlib.import_module(name)
    (sys.path.remove(path) for path in paths)
    return module
