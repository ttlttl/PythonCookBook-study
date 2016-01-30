#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
以*打头的参数只能作为最后一个位置参数出现，
以**打头的参数只能作为最后一个参数出现。
"""

"""
可接受任意数量位置参数的函数
"""
def avg(first, *rest):
    return(first + sum(rest))

if __name__ == '__main__':
    print(avg(1,2,3,4,5,6))