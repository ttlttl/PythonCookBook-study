#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
访问定义在闭包内的变量：
可以通过编写存取函数(getter/setter方法)并将它们作为函数属性附加到闭包上
"""

def sample():
    n = 0
    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
f.set_n(1000)
f()
print(f.get_n())



"""
使闭包模拟成类实例
"""
import sys

class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()

def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('hello')
print('len(s) = ',len(s))
print(s.pop())