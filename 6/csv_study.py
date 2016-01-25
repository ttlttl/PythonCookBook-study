#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print('Header:\n', headers)
    print('Rows:\n')
    for row in f_csv:
        print(row)

print('-'*20)
#namedtuple
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    Row = namedtuple('Row', headings)
    rows = [Row(*r) for r in f_csv]
    for row in rows:
        print(row.Symbol, row.Price)


print('-'*20)
#DictReader:
with open('stocks.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)

#Dump
with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rows = [row for row in f_csv]
with open('stocks2.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerow(rows)

#csv.DictWriter
