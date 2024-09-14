# 你需要并发执行的代码创建/销毁线程
# threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象。你可以创建一个 Thread 对象并将你要执行的对象以 target 参数的形式提供给该对象。


import time


def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


from threading import Thread

t = Thread(target=countdown, args=(10,))
t.start()

# 把一个线程加入到当前线程，并等待它结束 t.join()

# python解释器直到所有线程都终止前仍保持运行，对于需要长时间运行的线程或者需要一直运行的后台任务，应该考虑使用后台线程
# t = Thread(target=countdown, args=(10,), daemon=True)
# t.start()

# 后台线程无法等待，不过，这些线程会在主线程终止时自动 销毁


# 注意：
# 由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。所以，Python 的线程更适用于处理 I/O 和其他需要并发执行的阻塞操作（比如等待 I/O、等待从数据库获取数据等等），而不是需要多处理器并行的算密集型任务。

# 通过 multiprocessing 模块在一个单独的进程中执行你的代码

# import multiprocessing
# c = CountdownTask(5)
# p = multiprocessing.Process(target=c.run)
# p.start()
