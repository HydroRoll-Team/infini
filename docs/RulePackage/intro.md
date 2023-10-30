---
title: 概述
---

!!! abstract
    此章节涉及到真正的 Python 规范问题，因此请认真阅读并多加练习，方能写出漂亮的代码。

    
水系规则包可以通过 `pip` Pyhton 包管理工具直接下载，但是为了方便，我们推荐以下两个安装方案。

=== "Tab 1"

    Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
    { .annotate }

    1.  :man_raising_hand: I'm an annotation!

=== "Tab 2"

    Phasellus posuere in sem ut cursus (1)
    { .annotate }

    1.  :woman_raising_hand: I'm an annotation as well!


``` yaml
site_name: My Blog
theme:
  name: material
  features:
    - navigation.sections
plugins:
  - blog:
      blog_dir: . # (1)!
  - search
  - tags
nav:
  - index.md
```

1.  This is the important part – we're hosting the blog at the root of the
    project, and not in a subdirectory. For more information, see the
    [`blog_dir`][blog_dir] configuration option.

  [blog_dir]: ../../setup/setting-up-a-blog.md#+blog.blog_dir
