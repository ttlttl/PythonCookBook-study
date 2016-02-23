#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
对装饰器进行解包装。
如果装饰器的实现中已经使用了@wraps，可以通过__wrapped__属性来获取对原始数据的访问。
如果有多个装饰器已经作用于某个函数上，那么访问__wrapped__属性的行为是未定义的，应当避免这种情况。
"""

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y

add(2, 3)
add.__wrapped__(2, 3)