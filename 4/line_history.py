#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class LineHistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

if __name__ == '__main__':
    with open(__file__) as f:
        lines = LineHistory(f)
        for line in lines:
            if 'deque' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')