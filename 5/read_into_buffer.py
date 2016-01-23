#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用文件对象的readinto()方法将二进制数据直接读取到一个可变缓冲区中，不经过拷贝环节。
与read()方法不同，readinto()是为已存在的缓冲区填充内容，而不是分配新的对象然后再将它们返回，
用readinto()避免了产生额外的内存分配动作。
"""
import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

if __name__ == '__main__':
    buf = read_into_buffer(__file__)
    print(buf)