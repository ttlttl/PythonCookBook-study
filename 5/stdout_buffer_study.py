#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将字节数据写入打开的文本文件
"""
import sys

sys.stdout.buffer.write(b'hello,world\n')

#Error
sys.stdout.write(b'hello,world')