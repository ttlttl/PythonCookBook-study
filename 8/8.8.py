#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在子类中扩展属性
在子类中扩展父类中定义的某个功能
"""

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")



class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleteing name')
        super(SubPerson, SubPerson).name.__delete__(self)

a = SubPerson('Guido')
print(a.name)
a.name = 'Larry'
print(a.name)
a.name = 100

