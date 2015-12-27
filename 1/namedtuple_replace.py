#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用_replace填充具有可缺失字段的命名元组
"""
from collections import namedtuple

Stock = namedtuple('stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'hello', 'price': 100, 'date': '2015'}
print(dict_to_stock(a))

