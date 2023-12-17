---
title: 变更日志
---

# Changelog

## Infini

### [1.0.5](https://github.com/HydroRoll-Team/infini/compare/v1.0.4...v1.0.5) `<small>`December 18,2023`</small>`

**BREAKING CHANGES**

* Handler: 使用 `Handler` 代替 `Rule` ([`573a6`](https://github.com/HydroRoll-Team/infini/compare/7b219aa12949...540a3ee9bb81))。

**FEATURES**

* Handler: 实现泛型，实现 `self.stop()` `self.skip()` 方法  ([`573a6`](https://github.com/HydroRoll-Team/infini/compare/7b219aa12949...540a3ee9bb81))。

**BUG FIX**

* templates: 根据最新的 `Handler` 更新模板中的子类写法 ([`477c9`](https://github.com/HydroRoll-Team/HydroRollCore/commit/477c9ccfe4451920838705ab4aba81b2b41d0c50))。
* Event: 修订消息事件生成模式 ([`dd278`](https://github.com/HydroRoll-Team/infini/commit/dd27866fc9763af6f5b03024296dd74148d91eb3))，修复path不存在的问题 ([`5d4c7`](https://github.com/HydroRoll-Team/infini/commit/5d4c76a003a0f93ca52abe7f3997757ba66a97de))。

**CHORE**

* Exceptions: 重定义三个异常基类 ([`68ab4a`](https://github.com/HydroRoll-Team/HydroRollCore/commit/68ab4a7d835e7ede363d3bc9fa2731a4a335f4a0))。

### [1.0.4](https://github.com/HydroRoll-Team/infini/compare/v1.0.3...v1.0.4) `<small>`October 7,2023`</small>`

**FEATURES**

* Docs: 美化 `style`。
* Deps: 添加 `reportlab` 依赖，用于以后的 `pdf` 生成。

### [1.0.3](https://github.com/HydroRoll-Team/infini/compare/v1.0.2...v1.0.3) `<small>`October 7,2023`</small>`

**NO CHARGES**

### [1.0.2](https://github.com/HydroRoll-Team/infini/compare/v1.0.1...v1.0.2) `<small>`October 7,2023`</small>`

**FEATURES**

* Docs: 优化 `css` 细节。

### [1.0.1](https://github.com/HydroRoll-Team/infini/compare/v0.1.2...v1.0.1) `<small>`October 7,2023`</small>`

**BUG FIX**

* Docs: 修复 `Dev` 与 `latest` 分支的错别字。

### [0.1.2](https://github.com/HydroRoll-Team/infini/compare/v0.1.1...v0.1.2) `<small>`October 7,2023`</small>`

> 同步版本所做的测试。

### [0.1.1](https://github.com/HydroRoll-Team/infini/compare/v0.1.0...v0.1.1) `<small>`October 7,2023`</small>`

**BUG FIX**

* CLI: 添加命令行参数解析。

### [0.1.0-rc1](https://github.com/HydroRoll-Team/infini/compare/v0.1.0...v0.1.0-rc1) `<small>`October 7,2023`</small>`

**CHORE**

* README: 更新主页介绍的安装指南。

### [0.1.0](https://github.com/HydroRoll-Team/infini/commits/v0.0.1..v0.1.0) `<small>`October 7,2023 `</small>`

**FEATURES**

* CLI: 添加两个命令行名称 `infini` 与 `HRC`。

### [0.0.1](https://github.com/HydroRoll-Team/infini/commits/v0.0.1) `<small>`July 4,2023`</small>`

**FEATURES**

* __init__: 添加命令行参数解析。
* Rule: 添加 Rule 基类，实现读取指定文件夹下的 python 脚本或 python 包

**BREAKING CHANGE**

* infini: 添加命令行Path。
