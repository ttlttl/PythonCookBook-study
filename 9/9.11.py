#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
编写装饰器为被包装的函数添加参数。
为被包装的函数添加额外的参数.
很棒的功能！用来debug很方便！
"""
from functools import wraps

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

if __name__ == '__main__':
    @optional_debug
    def spam(a, b, c):
        print(a, b, c)

    spam(1, 2, 3)
    spam(1, 3, 3, debug=True)

