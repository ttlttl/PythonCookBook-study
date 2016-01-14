#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
函数中只要出现了yield语句就会将其转变成一个生成器。生成器只有在响应迭代操作时才运行。
"""
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

if __name__ == '__main__':
    for n in frange(0, 2, 0.1):
        print(n)