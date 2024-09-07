# 问题： 你构建了一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直接在你的这个新容器对象上执行迭代操作。

# 解决：实际上你只需要定义一个 __iter__() 方法，将迭代操作代理到容器内部的对象上去。


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node ({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        # iter(s) 只是简单的通过调用 s.__iter__() 方法来返回对应的迭代器对象，就跟 len(s) 会调用 s.__len__() 原理是一样的。
        return iter(self._children)


if __name__ == "__main__":
    node = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    node.add_child(child1)
    node.add_child(child2)

    for ch in node:
        print(ch)
