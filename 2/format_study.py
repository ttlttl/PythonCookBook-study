#!/usr/bin/env python
# -*- coding: utf-8 -*-

text = 'hello, world'

print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

print(format(text, '<20'))
print(format(text, '>20'))
print(format(text, '^20'))
print(format(text, '=>20'))
print(format(text, '*^20'))

a = 'hello'
b = 'world'
print('{}   {}'.format(b,a))

print(a,b, sep=':')

print('{ip}{version}'.format(ip='IP', version='v4'))

print('{a} {b}'.format_map(vars()))