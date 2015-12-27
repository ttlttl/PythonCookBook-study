#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
找出集合中的最大，最小的N个元素
heappop总是返回最小的元素。
"""
import heapq

nums = [1, 8 ,3, 11, -1, -3, 5, 9, 8]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print('-' * 20)

portfolio = [
    {'name': 'IBM', 'price': 20},
    {'name': 'HP', 'price': 30},
    {'name': 'DELL', 'price': 15},
    {'name': 'Cisco', 'price': 10},
    {'name': 'H3C', 'price': 22}
]
#key参数
print(heapq.nsmallest(3, portfolio, key=lambda s:s['price']))
print('-' * 20)

#heapify, heappop
#如果最大或最小的N个元素和总数比很小:
heap = list(nums)
heapq.heapify(heap)
while heap:
    print(heapq.heappop(heap), end=' ')