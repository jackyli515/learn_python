# 问题：你想反方向迭代一个序列
# 解决：使用内置的 reversed() 函数


a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)

# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊
# 方法时才能生效。如果两者都不符合，那你必须先将对象转换为一个列表才行，比如

# Print a file backwards
import os

os.path.abspath(__file__)
file_path = os.path.join(os.path.dirname(__file__), "../data_set", "somefile.txt")
f = open(file_path)
for line in reversed(list(f)):
    print(line, end="")


# 通过实现__reversed__() 特殊方法来实现反向迭代，示例：
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for rr in reversed(Countdown(30)):
    print(rr)

print("-" * 10)
for rr in Countdown(30):
    print(rr)
