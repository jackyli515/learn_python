# 问题 你需要对多线程程序中的临界区加琐以避免竞争条件
# 解决方案
# 在多线程程序中安全使用可变对象，我们需要使用threading库中的Lock对象，示例如下
import threading


class SharedCounter:

    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    # def incr(self, delta=1):
    #   self._value_lock.acquire()
    #   self._value += delta
    #   self._value_lock.release()

    def decr(self, delta=1):
        # Lock对象和With语句块一起使用可以保证互斥执行（就是每次只有一个线程可以执行with语句包含的代码块）
        # with语句会在这个代码执行前获得琐，在结束后释放琐
        with self._value_lock:
            self._value -= delta
