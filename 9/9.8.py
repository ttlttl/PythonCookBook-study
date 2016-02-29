#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在类中定义装饰器
"""

from functools import wraps

class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper

if __name__ == '__main__':
    a = A()
    @a.decorator1
    def spam():
        pass

    @A.decorator2
    def grok():
        pass

    spam()
    grok()