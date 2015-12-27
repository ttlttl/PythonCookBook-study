#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
去除重复元素，不改变剩余元素的顺序
"""
def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,9,1,3,5,6,6,0]
print(list(dedup(a)))