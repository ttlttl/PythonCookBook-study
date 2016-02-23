#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
元编程的主要目的是创建函数和类。
给函数添加一个包装。
装饰器就是一个函数，可以接受一个函数作为输入并返回一个新的函数作为输出
"""

import time
from functools import wraps

"""
定义一个装饰器函数
"""
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

"""
使用装饰器
"""
@timethis
def countdown(n):
    while n > 0:
        n -= 1

countdown(100000)
