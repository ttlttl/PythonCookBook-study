#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
应避免编写允许线程无限增长的程序，这种程序无法阻止恶意用户对服务器发起拒绝服务攻击。
"""

from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data

pool = ThreadPoolExecutor(10)
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.bing.com')
x = a.result()
y = b.result()
print(x, y)