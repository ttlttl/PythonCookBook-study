#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
对二进制文件做内存映射。
使用mmap可以高效而优雅^_^的对文件内容进行随机访问。
"""
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

if __name__ == '__main__':
    size = 1000000
    with open('data.tmp', 'wb') as f:
        f.seek(size-1)
        f.write(b'\x00')

    with memory_map('data.tmp') as m:
        print(len(m))
        print(m[0:10])
        m[0:12] = b'hello, world'
        m.close()

    with open('data.tmp', 'rb') as f:
        print(f.read(12))
