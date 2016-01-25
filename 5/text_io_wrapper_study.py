#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
为已经打开的文件添加或修改Unicode编码。
"""

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)