#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
对迭代器进行切片操作
"""

def count(n):
    while True:
        yield n
        n += 1

c =count(0)

import itertools
for x in itertools.islice(c, 10, 20):
    print(x, end=' ')
