#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('a@b.com', '2015')
print(sub)
print(sub.addr)
print(sub.joined)
#namedtuple是不可变的，可以用_replace()方法修改属性
sub = sub._replace(joined='2016')
print(sub)