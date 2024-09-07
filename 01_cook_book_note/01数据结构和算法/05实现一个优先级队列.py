# 问题： 怎样实现一个按优先级排序的队列？并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素

# 解决方案：利用 heapq 模块实现了一个简单的优先级队列

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # -priority优先级为负数的目的是使得元素按照优先级从高到低排序。这个跟普通的按优先级从低到高排序的堆排序恰巧相反。
        # index 变量的作用是保证同等优先级元素的正确排序。通过保存一个不断增加的index 下标变量，可以确保元素按照它们插入的顺序排序。而且，index 变量也在相同优先级元素比较的时候起到重要作用。
        # 如果你使用元组 (priority, item) ，只要两个元素的优先级不同就能比较。但是如果两个元素优先级一样的话，那么比较操作就会跟之前一样出错
        # 通过引入另外的 index 变量组成三元组 (priority, index, item) ，就能很好的避免上面的错误，因为不可能有两个元素有相同的 index 值。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return "Item({!r})".format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item("1foo"), 1)

    q.push(Item("5bar"), 5)
    q.push(Item("4spam"), 4)
    q.push(Item("grok"), 1)

    for i in range(4):
        print(f"{i},{q.pop()}")
