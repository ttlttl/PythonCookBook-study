#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定义一个属性可由用户修改的装饰器
"""
from functools import wraps, partial
import logging

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

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

        """
        set_level, set_message以属性的形式添加到了包装函数上
       """
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate

if __name__ == '__main__':
    @logged(logging.DEBUG)
    def add(x, y):
        return x + y

    @logged(logging.CRITICAL, 'example')
    def spam():
        print('Spam!')

    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)
    add.set_message('hello, world')
    add.set_level(logging.DEBUG)
    add(3, 4)