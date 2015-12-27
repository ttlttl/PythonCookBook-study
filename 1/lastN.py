#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输出匹配行前的N行
从队列两端添加或弹出元素的复杂的是O(1)，list的复杂度是O(N)
"""
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open(__file__) as f:
        for line, prevlines in search(f, 'here'):
            for pline in prevlines:
                print(pline)
            print(line, end='')
            print('-'*20)