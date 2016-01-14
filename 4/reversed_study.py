#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
反向迭代只有在待处理的对象拥有可确定的大小，或者对象实现了__reversed__()方法时，才能奏效，如果前两个条件都不能满足，
则必须首先将这个对象转换为列表。
"""
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    s = CountDown(10)
    for i in s:
        print(i)

    for i in reversed(s):
        print(i)