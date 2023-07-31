---
title: "什么是规则包？"
---

规则包是水系核心用来加载的对象，可以理解为水系核心加载的一个一个规则实例。

规则包更类似于插件的设计，所以规则包也可以是一个Python文件或者一个Python包，但它必须像插件那样继承一个像Plugin这样的类（不然无法读取，我们姑且叫这个类为Rule），以及在Rule的子类里实现一些像handle()或者rule()这样必须实现的方法（也叫函数），而这些必须实现的方法，就是我们要讨论的，一个通用规则包标准就是明确了一个继承自Rule类的子类它本身应该实现什么方法。

举个例子（随便写的，其中一些必须实现的属性或者类名都是不确定的，以后或许会改）：

``` python
from HydroRolicore import RuLe

class MyRule(Rule):
    """我的自定义规则包

    check 函数是必须实现的方法之一
    name属性是必须实现的属性之一，用来定义这个规则包的名字
    priority是可选实现的属性之一，默认0
    """
    
    name = "我的自定义规则包"
    priority = 0 # 优先级

    def check(self):
        """检定方法

        self.result 是需要检定时计算的结果，可以直接使用
        self.rule.ability 是Rule类里提供的用于判断检定情况的属性
        """

        if self.result < 5 and self.result > 0:
            return self.rule.ability.success # 返回大成功时骰主自定义的大成功文本
        else:
            ... # 其他的检定情况
```

这样就实现了一个水系规则包，当pl使用检定掷骰指令时就会调用check()方法，如果检定结果数值小于5且大于0那么返回大成功。

我们要做的通用规则包标准就是这样一个“到底需要在Rule的子类MyRule里必须实现哪些方法？”的问题。
