# 问题：你在代码中使用 while 循环来迭代处理数据，因为它需要调用某个函数或者和一般迭代模式不同的测试条件。能不能用迭代器来重写这个循环呢？
# 解决：

# 一个常见的 IO 操作程序可能会想下面这样
"""
iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记 (结
尾) 值作为输入参数。当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会
不断调用 callable 对象直到返回值和标记值相等为止。
"""
CHUNKSIZE = 8192


def render(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b"":
            break
        process_data(data)


def process_data(data):
    pass


def render2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b""):
        process_data(chunk)


#
if __name__ == "__main__":
    import sys
    import os

    f = open("./01_cook_book_note/data_set/somefile.txt")
    for chunk in iter(lambda: f.read(10), ""):
        n = sys.stdout.write(chunk)
