#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
跳过可迭代对象的前一部分元素
"""
import itertools

with open(__file__, encoding='utf-8') as f:
    for line in itertools.dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

print('\n' + '-'*20)

#跳过确定的行
with open(__file__, encoding='utf-8') as f:
    for line in itertools.islice(f, 5, None):
        print(line, end='')