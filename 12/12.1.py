#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
启动和停止线程.
由于GIL锁的存在，Python线程的执行模型被限制为在任意时刻只允许在解释器中运行一个线程，不应该使用Python线程处理
计算密集型的任务，适合用于I/O处理以及涉及阻塞操作的并发执行任务。
"""

import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

from threading import Thread
t=Thread(target=countdown, args=(10,))
t.start()