#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定义一个可接受参数的装饰器
"""

from functools import wraps
import logging

def logged(level, name=None, message=None):
    '''
    Add logging to a function.
    :param level:
    :param name:
    :param message:
    :return:
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

if __name__ == '__main__':
    @logged(logging.DEBUG)
    def add(x, y):
        return x + y

    @logged(logging.CRITICAL, 'example')
    def spam():
        print('Spam')

    add(3, 4)
    spam()
