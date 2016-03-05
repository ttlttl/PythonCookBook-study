#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
利用元类来控制实例的创建
改变实例创建的方式，以此来实现单例模式、缓存或者其他类似的特性。
"""

#通过定义一个元类并以某种方式重新实现它的__call__()方法定制创建实例。
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")

class Spam(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Spam.grok')

#可以调用静态方法，不能以普通的方式创建出实例。
Spam.grok(42)
#s = Spam()



#单例模式-类只能够创建唯一的一个实例
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
        else:
            return self.__instance

class Spam2(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

a = Spam2()
b = Spam2()

print(a is b)


#缓存
import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

class Spam3(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

a = Spam3('Guido')
b = Spam3('Diana')
c = Spam3('Guido')
print(a is b)
print(a is c)