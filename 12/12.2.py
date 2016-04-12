#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 判断线程是否已经启动.
 线程的核心特征是能够以非确定性的方式（即，何时开始，何时被打断，何时恢复执行完全由操作系统调度管理，用户无法确定）独立
 执行，如果程序中有其他线程需要判断某个线程是否已经到达执行过程中的某个点(线程同步问题)，可以使用threading库中的Event对象
"""
from threading import Thread, Event
import threading
import time

def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

started_evt = Event()

print('Launching countdown')
#主线程等待
t = Thread(target=countdown, args=(10, started_evt))
t.start()
started_evt.wait()
print('countdown is running')


"""
Event对象最好只用于一次性事件。
如果线程打算一遍又一遍重复通知某个事件，最好使用Condition对象来处理。
"""

