#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
迭代所有可能的组合或排列
"""

import itertools

items = ['a', 'b', 'c']
print('permutations(items):')
for p in itertools.permutations(items):
    print(p)

print('permutations(items, 2):')
for p in itertools.permutations(items, 2):
    print(p)

print('combinations(items, 3):')
for p in itertools.combinations(items, 3):
    print(p)

print('combinations(items, 2):')
for p in itertools.combinations(items, 2):
    print(p)

print('combinations_with_replacement(items,3):')
for p in itertools.combinations_with_replacement(items, 3):
    print(p)