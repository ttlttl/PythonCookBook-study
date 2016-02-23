#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
编写装饰器时如何保存函数的元数据。
当将装饰器用在一个函数上时，一些重要的元数据比如函数名，文档字符串，函数注解以及调用签名都会丢失。
每当定义一个装饰器时，应该总是记得为底层的包装函数添加functools库中的@wraps装饰器，这样会拷贝装饰器的元数据。
可以通过___wrapped__属性来访问被包装的那个函数。
"""

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@timethis
def countdown(n:int):
    """
    Count down
    :param n:
    :return:
    """
    """
    :param n:
    :return:
    """
    while n > 0:
        n -= 1

print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
countdown.__wrapped__(10000)