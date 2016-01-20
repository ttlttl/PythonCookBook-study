#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
yield from
扁平化处理嵌套的序列
"""
from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

if __name__ == '__main__':
    items = [1,2,[3,4,5,[6,7,8,9,[10,11,12],13],14,15],16,17]
    for x in flatten(items):
        print(x, end=' ')
