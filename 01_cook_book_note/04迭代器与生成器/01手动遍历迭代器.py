# 问题：你想遍历一个可迭代对象中的所有元素，但是却不想使用 for 循环。
# 解决： 为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常。
# 比如，下面的例子手动读取一个文件中的所有行：


def manual_iter():
    with open("/etc/passwd") as f:
        try:
            while True:
                # 通常来讲，StopIteration 用来指示迭代的结尾。然而，如果你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。
                line = next(f)
                # line = next(f, None)
                print(line, end=" ")
        except StopIteration:
            pass


def manual_iter2():
    with open("/etc/passwd") as f:
        while True:
            # 通常来讲，StopIteration 用来指示迭代的结尾。然而，如果你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None 。
            line = next(f, None)
            print(line, end=" ")


items = [1, 2, 3]
# 获取迭代器
it = iter(items)  # 调用 items.__iter__()

# 运行迭代器
print(next(it))

print(next(it))

print(next(it))  # 打印3

print(next(it))  # 抛出StopIteration异常
