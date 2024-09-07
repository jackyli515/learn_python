# 问题：你想将一个多层嵌套的序列展开成一个单层列表
# 解决方案: 可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题。

# yield和yield from 的区别
# yield 用于定义一个生成器函数
# 当函数执行到yield语句时，会暂停执行并返回一个值
# 下次迭代时，从上次暂停的地方继续执行

# yield from 用于调用另一个生成器函数
# 当执行到yield from语句时，会暂停并执行另一个生成器函数
# 另一个生成器完成后，当前生成器继续执行
# 简化生成器嵌套和传递的解决文案。减少代码重复，提高 了可读性和可维护性。


from collections.abc import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)  # 本句等价于下面这两句
            # for i in flatten(x):
            #     yield i
        else:
            yield x


items = [1, 2, [3, 4, [5, 6]], 7]

for x in flatten(items):
    print(x)
