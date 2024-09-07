# 问题：你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
# 解决：如果你想实现一种新的迭代模式，使用一个生成器函数yield来定义它。

# 一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。
# 一旦生成器函数返回退出，迭代终止。


# 下面是一个生产某个范围内浮点数的生成器
# 一个函数中需要有一个yield语句即可将其转换为一个生成器。跟普通函数不同的是，生成器只能用于迭代操作。
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


# 为了使用frange函数，我们可以用for循环来迭代它, 或者使用其他接受一个可迭代对象的函数（如sum(),list()等）,示例如下

for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))


# 下面用一个实验来展示yield语句将普通函数转换为一个生成器的底层工作机制
def countdown(n):
    print("Starting to count from", n)
    while n > 0:
        yield n
        n -= 1


c = countdown(3)
print(c)

# 运行到第1次yield语句，返回一个值
print(next(c))  # 3

# 运行到第2次yield语句，返回一个值
print(next(c))  # 2

# 运行到第3次yield语句，返回一个值
print(next(c))  # 1

print(next(c))  # Done和抛出异常StopIteration
