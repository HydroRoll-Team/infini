[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.poetry]
name = "HydroRollCore"
version = "0.1.1"
authors = ["简律纯 <i@jyunko.cn>"]
description = "Core of HydroRoll."
long_description = """
The long description of your project.
"""
keywords = ["HydroRoll", "core"]
homepage = "https://github.com/HydoRoll-Team/HydroRollCore"

[tool.poetry.dependencies]
python = ">=3.8"
tkinter = "^8.6.10"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.plugins."poetry-plugin"]
class = "poetry_plugin.plugin.Plugin"

[tool.poetry.plugins."poetry-plugin".scripts]
HydroRoll = "HydroRoll.__init__:main"
