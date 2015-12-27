#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter

rows = [
    {'name': 'c', 'id': 3},
    {'name': 'd', 'id': 2},
    {'name': 'a', 'id': 5},
    {'name': 'e', 'id': 6},
    {'name': 'f', 'id': 1}
]

rows_by_name = sorted(rows, key=lambda s: s['name'])
print(rows_by_name)

#Faster!!!
rows_by_id = sorted(rows, key=itemgetter('id'))
print(rows_by_id)