<p align="center">
  <a href="https://hydroroll.retrofor.space">
      <img src="https://hydroroll.retrofor.space/background_or_logo.png" height="128">
    <h1 align="center">HydroRoll'水系</h1>
  </a>
</p>

<p align="center">
  <a aria-label="Vercel Site" href="https://hydroroll.retrofor.space/" target="blank">
    <img src="https://img.shields.io/badge/DOCS%20AND%20BLOGS-000000.svg?logo=Vercel&labelColor=000">
  </a>
  <a aria-label="PYTHON version" href="https://pypi.org/project/hydrorollcore" target="blank">
    <img alt="" src="https://img.shields.io/pypi/v/hydroroll.svg?labelColor=000000">
  </a>
  <a aria-label="Join the community on GitHub" href="https://github.com/HydroRoll-Team/hydroroll/discussions" target="blank">
    <img alt="" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/CgoK/woKCv8GBgb/BgYG/woKCv8KCgr/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BgYG/0ZGRv9MTEz/JiYm/ygoKP9MTEz/RkZG/wYGBv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9ycnL/Li4u/1xcXP9eXl7/Li4u/3Jycv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP88PDz/cnJy/05OTv9OTk7/UFBQ/05OTv9wcHD/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Kioq/3Jycv9cXFz/TExM/05OTv9aWlr/cHBw/yoqKv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Pj4+/zg4OP+AgID/Pj4+/2ZmZv9oaGj/PDw8/4CAgP86Ojr/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/ywsLP9iYmL/enp6/zIyMv90dHT/dHR0/zAwMP98fHz/YmJi/ywsLP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9SUlL/PDw8/3Jycv9CQkL/UlJS/1RUVP9CQkL/cnJy/zw8PP9SUlL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/VFRU/yIiIv9aWlr/PDw8/zw8PP8+Pj7/PDw8/1hYWP8iIiL/VFRU/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/zQ0NP9CQkL/ZmZm/yIiIv9WVlb/WFhY/yIiIv9mZmb/QkJC/zY2Nv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9QUFD/BgYG/0RERP9KSkr/JCQk/yYmJv9KSkr/RERE/wgICP9QUFD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/CgoK/wICAv8KCgr/CgoK/wYGBv8GBgb/CgoK/woKCv8CAgL/CgoK/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==&labelColor=000000&logoWidth=20&logoColor=white">
  </a>
  <br></br>
  <a aria-label="Vercel Site" href="https://hydroroll.retrofor.space/" target="blank">
    <img src="https://img.shields.io/pypi/pyversions/hydroroll?labelColor=000000">
  </a>
    <a aria-label="License" href="https://github.com/HydroRoll-Team/hydroroll/blob/main/LICENSE" target="blank">
    <img alt="" src="https://img.shields.io/pypi/l/hydroroll.svg?labelColor=000000&color=">
  </a>
</p>

## 🎁 Getting

1. 安装库

在命令行输入。

``` shell
pip install HydroRollCore
```

2. 创建规则包实例

``` shell
mkdir myrules && cd myrules && mkdir rule1
echo.> config.toml && echo.> __init__.py :: 创建空的配置文件和python运行脚本
```

在 `__init__.py` 创建一个 `rule` 实例并继承 `Rule` 基类, 通过编写合适的相关方法与类注册规则包实现规则的自定义。

``` python
from hydrorollcore import Rule

class rule(Rule):
  ...

class Wiki(rule):
  ...
```

3. 合理修改你的 `config.toml` 配置文件，完成注册!

## 📄 License

[GPL 3.0](https://github.com/HydroRoll-Team/HydroRollCore/blob/main/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)
