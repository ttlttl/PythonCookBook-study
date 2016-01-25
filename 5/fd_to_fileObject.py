#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将已有的文件描述符包装为文件对象
"""
import os

fd = os.open(__file__, os.O_RDONLY)

f = open(fd, 'rt')
print(f.read())