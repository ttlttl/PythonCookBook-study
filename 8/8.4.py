#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建大量实例时节省内存
对于用作简单数据结构的类，可以在类定义中增加__slot__属性
"""

"""
当定义__slots__属性时，Python会针对实例采用一种更加紧凑的内部表示，不再让每个实例都创建一个__dict__字典，
现在的实例是围绕着一个固定长度的小型数组来构建的，在__slots__中列出的属性名会在内部映射到这个数组的特定索引上。
使用__slots__的副作用是不能再对实例添加任何新的属性。
"""
class Data:
    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


