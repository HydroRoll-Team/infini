---
title: attribute 属性
---

!!! info
    关联到一个对象的值，通常使用点号表达式按名称来引用。 举例来说，如果对象 o 具有属性 a 则可以用 o.a 来引用它。

    如果对象允许，将未被定义为 [标识符和关键字] 的非标识名称用作一个对象的属性也是可以的，例如使用 [setattr()]。 这样的属性将无法使用点号表达式来访问，而是必须通过 [getattr()] 来获取。

    [标识符和关键字]: https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#identifiers
    [setattr()]: https://docs.python.org/zh-cn/3/library/functions.html#setattr
    [getattr()]:https://docs.python.org/zh-cn/3/library/functions.html#getattr