#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用迭代器代替while循环。
iter可以选择性接受一个无参的可调用对象以及一个哨兵(结束)值作为输入，
当使用这种方式时，iter()会创建一个迭代器，然后重复调用用户提供的可迭代对象，直到返回哨兵值为止。
"""
import sys

if __name__ == '__main__':
    with open(__file__) as f:
        f = open(__file__)
        for chunk in iter(lambda: f.read(10), ''):
            sys.stdout.write(chunk)