#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用__repr__()返回的是实例的代码表示，通常可以用它返回的字符串文本来重新创建这个实例。
__str__()将实例转换为一个字符串，这也是用str()和print()函数所产生的输出。

对于__repr__()，标准的做法是让它产生的字符串文本能满足eval(repr(x)) == x,
如果不能做到或者不希望有这种行为，通常让它产生一段有帮助意义的文本，以<>括起来。
如果没有定义__str__(),那么就用__repr__的输出当做备份。
"""

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)

print(p)
print(repr(p))

#!r表示应该使用__repr__()的输出，而不是默认的__str__()
print('p is {0!r}'.format(p))