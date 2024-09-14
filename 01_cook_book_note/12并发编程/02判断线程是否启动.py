# 你已经启动了一个线程，但是你想知道它是不是真的已经开始运行了。
# 线程的一个关键特性是每个线程都是独立运行且状态不可预测。如果程序中的其
# 他线程需要通过判断某个线程的状态来确定自己下一步的操作，这时线程同步问题就
# 会变得非常棘手。

# 为了解决这些问题，我们需要使用 threading 库中的 Event 对象。
# Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。
# 在初始情况下，event 对象中的信号标志被设置为假。如果有线程等待一个 event 对象，而这个 event 对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。一个线程
# 如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待这个 event 对象的线程。

from threading import Thread, Event
import time


# Code to execute in an independent thread
def countdown(n, started_evt):
    print("countdown starting")
    started_evt.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
started_evt = Event()
# Launch the thread and pass the startup event
print("Launching countdown")
t = Thread(target=countdown, args=(10, started_evt))
t.start()
# Wait for the thread to start
started_evt.wait()
print("countdown is running")


# 如果一个线程需要不停地重复使用 event 对象，你最
# 好使用 Condition 对象来代替。下面的代码使用 Condition 对象实现了一个周期定时
# 器，每当定时器超时的时候，其他线程都可以监测到
