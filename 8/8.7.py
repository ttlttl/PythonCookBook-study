#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
调用父类中的方法
调用父类中的在子类中被覆盖的方法，用super()
"""
class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


a = A()
b = B()

a.spam()
b.spam()


"""
super()的常见用途是调用父类的__init__()方法，确保父类被正确的初始化
"""
class AA:
    def __init__(self):
        self.x = 0

class BB(AA):
    def __init__(self):
        super().__init__()
        self.y = 1


bb = BB()
print(bb.x, bb.y)


"""
另一种常见用途是在当覆盖了Python中的特殊方法时
"""
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, name, value):
        return getattr(self._obj, name)

    """
    对名称进行检查
    """
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            setattr(self._obj, name, value)

