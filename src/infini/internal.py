from infini.loader import Loader
from infini.register import Register
from infini.typing import List, Optional
from pathlib import Path

import sys
import inspect


def require(name: str, paths: Optional[List] = None) -> Register:
    caller_frame = inspect.stack()[1][0]
    caller_file = caller_frame.f_globals["__file__"]

    default_paths = [Path(caller_file).resolve().parent]
    paths = [
        str(path)
        for path in ((list(paths) + default_paths) if paths else default_paths)
    ]
    (sys.path.insert(0, path) for path in paths)

    with Loader() as loader:
        loader.load(name)
        sys.path = sys.path[len(paths) - 1 :]
        register = loader.into_register()

    caller_frame.f_globals[f"{name}_register"] = register
    return register
