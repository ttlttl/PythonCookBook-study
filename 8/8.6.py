#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建可管理的对象
property
实际上是把一系列方法绑定到一起value.fget, value.fset, value.fdel
"""

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Cant't delete attribute")

"""
对于以存在的get和set方法，也可以定义为property
"""
class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, del_first_name)

a = Person('Guido')
print(a.first_name)
a.first_name = 88
