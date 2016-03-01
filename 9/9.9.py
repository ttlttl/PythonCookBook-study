#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
把装饰器定义成类
需要在类中实现__call__()和__get__()方法
"""

import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

if __name__ == '__main__':
    @Profiled
    def add(x, y):
        return x + y

    class Spam:
        @Profiled
        def bar(self, x):
            print(self, x)

    print(add(2, 3))
    print(add(4, 5))
    print(add.ncalls)
    s = Spam()
    print(s.bar(1))
    print(s.bar(2))
    print(Spam.bar.ncalls)
