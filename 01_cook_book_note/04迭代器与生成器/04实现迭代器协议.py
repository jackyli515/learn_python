# 问题：你想构建一个能支持迭代操作的自定义对象，并希望找到一个能实现迭代协议的简单方法。

# 解决：目前为止，在一个对象上实现迭代最简单的方式是使用一个生成器函数。


"""
DepthFirstIterator 类和上面使用生成器的版本工作原理类似，但是它写起来很
繁琐，因为迭代器必须在迭代处理过程中维护大量的状态信息。坦白来讲，没人愿意写
这么晦涩的代码。将你的迭代器定义为一个生成器后一切迎刃而解。
  """
class Node:
  def __init__(self, value):
    self._value = value
    self._children = []
  def __repr__(self):
    return 'Node({!r})'.format(self._value)
  def add_child(self, node):
    self._children.append(node)
  def __iter__(self):
    return iter(self._children)

  # 它首先返回自己本身并迭代每一个子节点并通过调用子节点的 depth_first() 方法 (使用 yield from 语句) 返回对应元素。
  def depth_first(self):
    yield self
    for c in self:
      yield from c.depth_first()


class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return "Node({!r})".format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):

    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # 刚开始返回自身；并为children创建一个迭代器
        if self._children_iter is None:
            self._children_iter = iter(self._node)

            return self._node
        # 如果 处理一个子节点，则返回下一个子节点
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
        # # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)

    next = __next__


# Example
if __name__ == '__main__':
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
child1.add_child(Node(3))
child1.add_child(Node(4))
child2.add_child(Node(5))
for ch in root.depth_first():