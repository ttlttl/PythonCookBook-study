#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open(__file__) as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass
print('\n'+'-'*20)
with open(__file__) as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')