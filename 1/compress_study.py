#!/usr/bin/env python
# -*- coding: utf-8 -*-
#itertools.compress 筛选出满足布尔序列的值，返回一个迭代器
from itertools import compress

a = ['a', 'b', 'c', 'd']
b = [True, False, False, True]

print(list(compress(a, b)))