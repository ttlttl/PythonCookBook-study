#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
heapq.merge对所有提供的序列不会一次性读取，可以处理非常长的序列，开销比较小。
heapq.merge要求所有的输入序列都是有序的。
"""
import heapq

a = [1,2,3,4]
b = [5,6,7,8]

for i in heapq.merge(a, b):
    print(i, end=' ')