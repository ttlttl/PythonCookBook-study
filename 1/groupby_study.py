#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '23', 'date': '2013'},
    {'address': '32', 'date': '2012'},
    {'address': '13', 'date': '2011'},
    {'address': '13', 'date': '2012'},
    {'address': '44', 'date': '2013'},
    {'address': '35', 'date': '2014'},
    {'address': '63', 'date': '2015'},
    {'address': '62', 'date': '2012'},
    {'address': '15', 'date': '2013'}
]

#groupby只能检查连续的项
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(' ', item)