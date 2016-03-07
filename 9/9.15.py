#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
定义一个能接受可选参数的元类。
Python允许在class语句中通过使用metaclass关键字参数来指定元类。
"""

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


#在自定义的元类中还可以提供额外的关键字参数, 需要保证在定义__prepare__(),
# __new__()以及__init__()方法时使用keyword-only参数指定它们。
class MyMeta(type):
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        super().__init__(name, bases,ns)

