#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用装饰器给类定义打补丁。
"""

#使用__getattribute__修改类的行为
def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting: ', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls

if __name__ == '__main__':
    @log_getattribute
    class A:
        def __init__(self, x):
            self.x = x

        def spam(self):
            pass

    a = A(42)
    print(a.x)
    print(a.spam())