# 问题：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？


from collections import deque


# 在多行上面做简单的文本匹配，并返回匹配所在行的最后 N 行：
def search(lines, pattern, history=5):
    # 使用 deque(maxlen=N) 构造函数会新建一个固定大小的队列
    # 当新的元素加入并且这个队列已满的时候，最老的元素会自动被移除掉。
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            # yield 迭代器
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    import os

    file_path = os.path.join(os.path.dirname(__file__), "../data_set", "somefile.txt")
    with open(file_path) as f:
        for line, prevlines in search(f, "python", 5):
            for pline in prevlines:
                print(pline, end="")

"""
# 学习笔记
1.写查询元素的代码时，通常会使用包含 yield 表达式的生成器函数，也就
是我们上面示例代码中的那样。
2.deque 类可以被用在任何你只需要一个简单队列数据结构的场合。你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添
加和弹出元素的操作


"""
