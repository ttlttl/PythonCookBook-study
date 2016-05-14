#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
对临界区加锁
"""
import threading
import time

class SharedCounter:
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    #当使用with语句时，Lock对象可确保产生互斥的行为，也就是同一时间只允许一个线程执行with语句块中的代码。
    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta

    def value(self):
        with self._value_lock:
            return self._value

def func(counter):
    thread = threading.current_thread()
    id = thread.name
    time.sleep(1)
    for i in range(10):
        counter.incr()
        print("Thread %s, value %s" % (id, counter.value()))

if __name__ == '__main__':
    counter = SharedCounter()
    t1 = threading.Thread(target=func, args=(counter,))
    t2 = threading.Thread(target=func, args=(counter,))
    t3 = threading.Thread(target=func, args=(counter,))
    t4 = threading.Thread(target=func, args=(counter,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()