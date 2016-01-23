#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用partial对一系列固定大小的记录或数据块进行迭代，如果文件大小不是记录的整数倍，最后产生的数据块会比期望的少。
iter()函数，如果传入一个可调用对象，以及一个哨兵值给它，那么它可以创建一个迭代器，
得到的迭代器会重复调用用户提供的可迭代对象，直到返回的值为哨兵值为止，此时迭代过程停止。
"""
from functools import partial

RECORD_SIZE = 5

with open(__file__, 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)