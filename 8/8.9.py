#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建一种新形式的类属性或实例属性.
若要创建一个新形式的实例属性，可以以描述符类的形式定义其功能。
描述符就是以特殊方法 __set__, __get__, __delete__的形式实现的属性访问操作的类。。，
"""
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 3)
print(p.x)
print(p.y)
p.x = 1.1