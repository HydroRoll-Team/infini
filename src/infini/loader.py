from importlib.util import spec_from_file_location
from infini.core import Core
from infini.generator import TextGenerator
from infini.handler import Handler
from infini.interceptor import Interceptor
from infini.register import Register
from infini.typing import List, Dict, Sequence, ModuleType, RouterType, Callable
from infini.logging import logger
from pathlib import Path

import inspect
import sys
import importlib
import importlib.abc


class InfiniMetaFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname: str, path: Sequence[str] | None, target=None):
        default_entries = [
            Path.cwd() / "src",
            Path.home() / ".ipm" / "src",
        ] + [Path(path).resolve() for path in sys.path]

        entries: List[Path] = (
            [Path(catch_path).resolve() for catch_path in path] + default_entries
            if path
            else default_entries
        )

        if "." in fullname:
            *_, name = fullname.split(".")
        else:
            name = fullname

        for entry in entries:
            if (entry / name).is_dir():
                filename = entry / name / "src" / "__init__.py"
                submodule_locations = [entry / name / "src"]
                if not filename.exists():
                    filename = entry / name / "src" / (name + ".py")
            else:
                continue
            if not filename.exists():
                continue

            return spec_from_file_location(
                fullname,
                filename,
                loader=InfiniLoader(str(filename)),
                submodule_search_locations=[
                    str(submodule_location)
                    for submodule_location in submodule_locations
                ]
                if submodule_locations
                else None,
            )

        return None


class InfiniLoader(importlib.abc.Loader):
    def __init__(self, filename):
        self.filename = filename

    def create_module(self, _):
        return None

    def exec_module(self, module):
        exec(Path(self.filename).read_text("utf-8"), vars(module))


def install():
    sys.meta_path.insert(0, InfiniMetaFinder())


def uninstall():
    for meta_path in sys.meta_path:
        if isinstance(meta_path, InfiniMetaFinder):
            sys.meta_path.remove(meta_path)
            break


class Loader:
    pre_interceptors: List[RouterType]
    handlers: List[RouterType]
    events: Dict[str, str]
    global_variables: Dict[str, str | Callable]
    interceptors: List[RouterType]

    def __init__(self) -> None:
        self.pre_interceptors = []
        self.handlers = []
        self.events = {}
        self.global_variables = {}
        self.interceptors = []
        self.prepare()

    def __enter__(self) -> "Loader":
        self.prepare()
        return self

    def __exit__(self, exc_type, exc_value, _) -> None:
        self.close()
        if exc_type is not None:
            raise exc_type(exc_value)

    def _find_register_variables(self, module: ModuleType) -> List[Register]:
        module_variables = inspect.getmembers(module)
        register_variables = [
            var for _, var in module_variables if isinstance(var, Register)
        ]
        return register_variables

    def prepare(self) -> None:
        install()

    def load(self, name: str) -> ModuleType:
        self.prepare()

        module = importlib.import_module(name)
        registers = self._find_register_variables(module)
        self.load_from_registers(registers)
        if not registers:
            logger.warning(
                f"Infini 装载器未能在规则包 [bold green]{module.__name__}[/bold green] 中找到注册器."
            )

        return module

    def load_from_registers(self, registers: Sequence[Register]):
        for register in registers:
            self.load_from_register(register)

    def load_from_register(self, register: Register):
        self.pre_interceptors.extend(register.pre_interceptors)
        self.handlers.extend(register.handlers)
        self.events.update(register.events)
        self.global_variables.update(register.global_variables)
        self.interceptors.extend(register.interceptors)

    def close(self):
        uninstall()

    def inject_core(self, core: Core):
        pre_interceptor = Interceptor()
        handler = Handler()
        generator = TextGenerator()
        interceptor = Interceptor()

        self.inject_pre_interceptor(pre_interceptor)
        self.inject_handler(handler)
        self.inject_generator(generator)
        self.inject_interceptor(interceptor)
        core.pre_interceptor = pre_interceptor
        core.handler = handler
        core.generator = generator
        core.interceptor = interceptor

    def into_core(self) -> Core:
        core = Core()
        self.inject_core(core)
        return core

    def inject_register(self, register: Register):
        register.pre_interceptors = self.pre_interceptors
        register.handlers = self.handlers
        register.events = self.events
        register.global_variables = self.global_variables
        register.interceptors = self.interceptors

    def into_register(self) -> Register:
        register = Register()
        self.inject_register(register)
        return register

    def inject_interceptor(self, interceptor: Interceptor):
        interceptor.interceptors = self.interceptors

    def into_interceptor(self) -> Interceptor:
        interceptor = Interceptor()
        self.inject_interceptor(interceptor)
        return interceptor

    def inject_handler(self, handler: Handler):
        handler.handlers = self.handlers

    def into_handlers(self) -> Handler:
        handler = Handler()
        self.inject_handler(handler)
        return handler

    def inject_generator(self, generator: TextGenerator):
        generator.events = self.events
        generator.global_variables = self.global_variables

    def into_generator(self) -> TextGenerator:
        generator = TextGenerator()
        self.inject_generator(generator)
        return generator

    def inject_pre_interceptor(self, pre_interceptor: Interceptor):
        pre_interceptor.interceptors = self.pre_interceptors

    def into_pre_interceptor(self) -> Interceptor:
        pre_interceptor = Interceptor()
        self.inject_pre_interceptor(pre_interceptor)
        return pre_interceptor
