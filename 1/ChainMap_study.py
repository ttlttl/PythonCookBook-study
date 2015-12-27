#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将多个字典或映射在逻辑上合并成一个单独的映射结构
如果有重复的键，则会采用第一个映射中对应的值

两个字典合并a.update(b)
"""
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
for k, v in c.items():
    print(k, v)
