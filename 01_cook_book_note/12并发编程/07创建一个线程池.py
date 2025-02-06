# 问题 你创建一个工作者线程池，用来相应客户端请求或执行其他的工作

# 解决方案
# concurrent.futures 函数库有一个ThreadPoolExecutor类，可以被用来完成这个任务

# 示例 一个简单的TCP服务器，使用了一个线程池来响应客户端

from queue import Queue
from threading import Thread

nworkers = 16
q = Queue()
for n in range(nworkers):
    t = Thread(target=echo_client, args=(q,))

    t.daemon = True
    t.start()
