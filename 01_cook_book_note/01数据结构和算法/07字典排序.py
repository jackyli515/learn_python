"""
问题
你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

解决方案
为 了 能 控 制 一 个 字 典 中 元 素 的 顺 序， 你 可 以 使 用 collections 模 块 中 的OrderedDict 类。在迭代操作的时候它会保持元素被插入时的顺序，

"""

from collections import OrderedDict

# 保持字典插入顺序
d = OrderedDict()

d["foo"] = 1
d["bar"] = 2
d["spam"] = 3
d["grok"] = 4

for key in d:
    print(key, d[key])


# 序列化后仍然保持字典顺序

import json

print(json.dumps(d))
