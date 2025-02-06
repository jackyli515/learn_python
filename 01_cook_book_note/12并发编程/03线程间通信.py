#  我们的程序中有多个线程，需要在这些线程间安全交换信息或数据
# 解决方案：
# 从一个线程向另一个线程发送数据最安全的方式可能就是使用queue库中的队列了。
# 创建一个被多个线程共享的Queue对象，然后使用put()和get()方法来向队列中添加和获取数据。

from queue import Queue
from threading import Thread


# 生产数据的线程
def producer(out_q):
    while True:
        out_q.put(42)


# 消费数据的线程
def consumer(in_q):
    while True:
        print(in_q.get())


q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()

t2.start()

# Queue对象已经包含了必要的锁，所以我们可以通过它在多个线程间安全地共享数据。当使用队列时，协调生产者和消费者的关闭问题可能会有一些麻烦。
# 解决：在队列中旋转一个特殊的值，当消费者讲到这个值时，终止执行。
