#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
StringIO
BytesIO
没有真正的文件描述符
"""
import io

s = io.StringIO()
s.write('hello, world\n')
print('hello, again', file=s)

print(s.getvalue())