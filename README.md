<h1 align="right">infini'水系核心</h1>

<p align="right">
    <a aria-label="Join the community on GitHub" href="https://github.com/HydroRoll-Team/hydroroll/discussions" target="blank">
        <img alt="" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8CAgL/CgoK/woKCv8GBgb/BgYG/woKCv8KCgr/AgIC/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/BgYG/0ZGRv9MTEz/JiYm/ygoKP9MTEz/RkZG/wYGBv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9ycnL/Li4u/1xcXP9eXl7/Li4u/3Jycv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP88PDz/cnJy/05OTv9OTk7/UFBQ/05OTv9wcHD/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Kioq/3Jycv9cXFz/TExM/05OTv9aWlr/cHBw/yoqKv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/Pj4+/zg4OP+AgID/Pj4+/2ZmZv9oaGj/PDw8/4CAgP86Ojr/Pj4+/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/ywsLP9iYmL/enp6/zIyMv90dHT/dHR0/zAwMP98fHz/YmJi/ywsLP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9SUlL/PDw8/3Jycv9CQkL/UlJS/1RUVP9CQkL/cnJy/zw8PP9SUlL/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/VFRU/yIiIv9aWlr/PDw8/zw8PP8+Pj7/PDw8/1hYWP8iIiL/VFRU/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/zQ0NP9CQkL/ZmZm/yIiIv9WVlb/WFhY/yIiIv9mZmb/QkJC/zY2Nv8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP9QUFD/BgYG/0RERP9KSkr/JCQk/yYmJv9KSkr/RERE/wgICP9QUFD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/CgoK/wICAv8KCgr/CgoK/wYGBv8GBgb/CgoK/woKCv8CAgL/CgoK/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==&labelColor=000000&logoWidth=20&logoColor=white">
    </a>
    <a href="https://pypi.org/project/infini">
        <img alt="pypi" src="https://img.shields.io/pypi/v/infini?labelColor=000000">
    </a>
    <a href="https://github.com/HydroRoll-Team/infini/blob/master/LICENSE">
        <img alt="hydro" src="https://img.shields.io/pypi/l/infini.svg?labelColor=000000&color=">
    </a>

[![.github/workflows/python-publish.yml](https://github.com/HydroRoll-Team/infini/actions/workflows/python-publish.yml/badge.svg)](https://github.com/HydroRoll-Team/infini/actions/workflows/python-publish.yml)
[![CodeQL](https://github.com/HydroRoll-Team/infini/actions/workflows/codeql.yml/badge.svg)](https://github.com/HydroRoll-Team/infini/actions/workflows/codeql.yml)
[![Netlify Status](https://api.netlify.com/api/v1/badges/ecbe4af3-223f-4fa4-a182-a37a776fd05b/deploy-status)](https://app.netlify.com/sites/grps-v1/deploys)

</p>

## 🎁 Getting <img align="right" alt="hydro" src="https://mirror.ghproxy.com/https://raw.githubusercontent.com/HydroRoll-Team/HydroRoll/main/site/src/assets/image/logo.png" height="120">

> [!IMPORTANT]  
>
> 强烈推荐使用 `pdm` 等能创建虚拟环境的包管理工具管理你的 `HydroRollBot` 项目。

1. 安装库

    在终端中执行：

    ```bash
    git clone https://github.com/HydroRoll-Team/infini.git
    cd infini
    pdm install
    ```

    你可以使用`pip`进行安装：

    ```bash
    pip install infini
    ```

2. 创建规则包实例

    创建`cli.py`并写入以下内容：

    ```python
    import infini

    client = infini.Cli()
    client.parse_args()
    ```

    打开终端并执行：

    ``` shell
    python cli.py --new --path MyRule
    ```

    你可以在生成的 `MyRule\rule.py` 创建一个或者多个 `rule` 实例并继承 `Rule` 基类, 通过编写合适的相关方法与类注册规则包实现规则的自定义。

    ``` python
    from infini import Rule, Result, Dice

    class MyRule(Rule):
        """自设规则包"""

        name = "MyRule"
        priority: int = 0

        def __init__(self) -> None:
            """初始化你的规则包"""

        def check(self, dice: Dice) -> Result:
            """声明规则包检定方式"""
            return Result("event1", True)
    ```

    `check`函数应当返回一个`Result`对象，它应当包含一个消息事件名（例如示例中的`event1`），该消息事件名应当在 `MyRule\event.py` 中被注册。消息事件的动态内容通过`{name}`的方式声明并通过`name="内容"`的方式实现。

3. 合理修改你的 `config.toml` 配置文件，完成注册!

### 🎍Sites

<https://grps.hydroroll.team> _(recommend)_  
<https://grps-v1.netlify.app>  
~~<https://hydroroll-team.github.io/infini/>~~

## 📄 License

[MIT](https://github.com/HydroRoll-Team/infini/blob/master/LICENSE) © 2023-PRESENT [简律纯](https://github.com/HsiangNianian)
