#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用类中定义的__format__()方法自定义字符串的输出格式。
"""

_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2016, 2, 3)
print(format(d))

print(format(d, 'mdy'))

print('The date is {:ymd}'.format(d))