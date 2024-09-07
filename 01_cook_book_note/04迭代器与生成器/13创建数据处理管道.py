# 问题：你想以数据管道 (类似 Unix 管道) 的方式迭代处理数据。比如，你有个大量的数据需要处理，但是不能将它们一次性放入内存中。
# 解决：生成器函数是一个实现管道机制的好办法。
# 为了演示，假定你要处理一个非常大的日志文件目录
"""
foo/
  access-log-012007.gz
  access-log-022007.gz
  access-log-032007.gz
  ...
  access-log-012008
bar/
  access-log-092007.bz2
  ...
  access-log-022008
"""
# 假设每个日志文件包含这样的数据：
"""
124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369
61.135.216.105 - - [10/Jul/2012:00:20:04 -0500] "GET /blog/atom.xml ..." 304 -
...
"""

import fnmatch
import gzip
import bz2
import re
import os


# 为了处理这些文件，你可以定义一个由多个执行特定任务独立任务的简单生成器函数组成的容器
def gen_find(filepat, top):
    """
    在指定目录树中查找所有满足通配符的文件名
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    在每次产一个对象时打开一个文件，并在下一次调用next函数时，立即关闭
    """
    for filename in filenames:
        if filename.endswith(".gz"):
            f = gzip.open(filename, "r")
        elif filename.endswith(".bz2"):
            f = bz2.open(filename, "r")
        else:
            f = open(filename, "r")
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    把多个迭代器链接成一个迭代器
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    查找匹配的行
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 查找包含python的所有日志行：
lognames = gen_find("access-log*", "www")
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep("(?i)python", lines)
for line in pylines:
    print(line)

# 示例：计算这个版本传输的字节数并计算其总和
lognames = gen_find("access-log*", "www")
files = gen_opener(lognames)
lines = gen_concatenate(files)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != "-")
print("Total", sum(bytes))
