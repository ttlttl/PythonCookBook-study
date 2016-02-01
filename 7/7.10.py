#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
在回调函数中携带额外的状态
"""
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def print_result(result):
    print('GOT: ', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)


"""
一种在回调函数中携带额外信息的方法是使用绑定方法
"""
class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] GOT: {}'.format(self.sequence, result))

r = ResultHandler()
apply_async(add, (3, 4), callback=r.handler)
apply_async(add, ('hello, ', 'world'), callback=r.handler)

"""
另一种是使用闭包
"""
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence #nonlocal声明用来表示变量在回调函数中修改
        sequence += 1
        print('[{}] got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, ('bi', 'bao'), callback=handler)
apply_async(add, ('bao', 'bi'), callback=handler)

"""
另一种方法，协程
"""
def make_coroutine_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] gOt: {}'.format(sequence, result))

handler = make_coroutine_handler()
next(handler) #启动
apply_async(add, ('hello, ', 'coroutine'), callback=handler.send)
apply_async(add, ('coroutine, ', 'hello'), callback=handler.send)

"""
还可以使用partial
"""
class SequenceNo:
    def __init__(self):
        self.sequence = 0

def handler(result, seq):
    seq.sequence += 1
    print('[{}] goT: {}'.format(seq.sequence, result))

seq = SequenceNo()
from functools import partial
apply_async(add, ('hello, ', 'partial'), callback=partial(handler, seq=seq))
apply_async(add, ('hello, ', 'partial'), callback=partial(handler, seq=seq))





