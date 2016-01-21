#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
file=f将输出重定向。
"""
with open(__file__, 'at') as f:
    print("\n    print('hello')", file=f)

