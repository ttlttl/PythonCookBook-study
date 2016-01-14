#!/usr/bin/env python
# -*- coding: utf-8 -*-

my_list = ['a', 'b', 'c']

for i, v in enumerate(my_list):
    print(i, v)

for i, v in enumerate(reversed(my_list), 1):
    print(i, v)