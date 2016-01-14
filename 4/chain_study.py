#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chain(a, b) 不需要a,b是同一类型
a+b 需要a,b是同一类型，产生一个新的序列，开销大
"""
import itertools

a = [1,2,3,4]
b = ['a', 'b', 'c']
c = 'hello'

for i in itertools.chain(a, b, c):
    print(i)