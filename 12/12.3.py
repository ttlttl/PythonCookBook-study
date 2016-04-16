#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
线程间通信
最安全的做法是使用queue模块中的Queue，首先创建一个Queue实例，它会被所有的线程共享，
之后线程可以使用put()或get()操作给队列添加或移除元素。
Queue实例已经拥有所有需要的锁，它们可以安全的在任意多 的线程之间共享。
当使用队列时，可以使用特殊的终止值对生产者消费者的关闭过程进行同步协调。
"""

from queue import Queue
from threading import Thread

_sentinel = object()

def producer(out_q):
    for i in range(10):
        out_q.put('hello')
    out_q.put(_sentinel)

def consumer(in_q):
    while True:
        data = in_q.get()
        if data is _sentinel:
            #消费者接收到这个特殊终止值后会立刻将其重新放回队列中，
            #使得在同一队列上监听的其他消费者线程也能收到终止值。
            in_q.put(_sentinel)
            break
        print(data)

q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()