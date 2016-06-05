#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
避免死锁的一种方案就是给程序中的每个锁分配一个唯一的数字编号，并且在获取多个锁时只按照编号的升序方式来获取。
"""

import threading
from contextlib import contextmanager

_local = threading.local()


@contextmanager
def acquire(*locks):
    locks = sorted(locks, key=lambda x : id(x))
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]

if __name__ == '__main__':
    x_lock = threading.Lock()
    y_lock = threading.Lock()

    def thread_1():
        while True:
            with acquire(x_lock, y_lock):
                print('Thread-1')

    def thread_2():
        while True:
            with acquire(y_lock, x_lock):
                print('Thread-2')

    t1 = threading.Thread(target=thread_1)
    t1.daemon = True
    t1.start()
    t2 = threading.Thread(target=thread_2)
    t2.daemon = True
    t2.start()

