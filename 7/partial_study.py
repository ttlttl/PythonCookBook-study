#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用partial使可调用对象以较少的参数形式调用
"""
from functools import partial
import math

def spam(a, b, c, d):
    print(a, b, c, d)

s1 = partial(spam, 1)
s1(2,3,4)

s2 = partial(spam, d=4)
s2(1,2,3)

s3 = partial(spam, 1, 2, d=4)
s3(3)


"""
list的sort方法可接受一个key参数，它可以用来做自定义的排序处理，但是key只能是接收单参数的函数，
可使用partial使之相容。
"""
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)

"""
partial()常常用来调整其他库中用到的回调函数的参数签名。
"""


