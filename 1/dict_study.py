#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

#创建单键对多值，值有序字典
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)

#创建单键对多值，无序集合
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)

#普通字典调用setdefault()
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)

#两个字典的相同之处
a={
    'x': 1,
    'y': 2,
    'z': 3
}

b={
    'x': 2,
    'y': 2,
    'w': 5
}
print(a.keys() & b.keys())
print(a.items() & b.items())
print('-' * 20)
#过滤
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(c)