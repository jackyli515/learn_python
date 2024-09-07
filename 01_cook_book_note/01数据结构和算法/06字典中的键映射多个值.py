# 问题: 怎样实现一个键对应多个值的字典（也叫 multidict）？
# 解决方案: 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中，比如列表或者集合里面。
"""
d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}
"""

# 使用 collections 模块中的 defaultdict 来构造这样的字典
from collections import defaultdict

# 需要注意的是，defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(4)
d = defaultdict(set)
d["a"].add(1)
d["a"].add(2)
d["b"].add(4)

# 普通的字典上使用 setdefault() 方法来代替
d = {}  # A regular dictionary
d.setdefault("a", []).append(1)
d.setdefault("a", []).append(2)
d.setdefault("b", []).append(4)

# 对比
pairs = {"a": 1, "b": 2}
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# 如果使用 defaultdict 的话代码就更加简洁了
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
