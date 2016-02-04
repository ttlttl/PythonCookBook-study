#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
让对象支持上下文管理协议(支持with语句)
需要实现__enter__和__exit__()方法
上下文管理器常用在需要管理类似文件，网络连接和锁这样的资源的程序中。
"""
from socket import socket, AF_INET, SOCK_STREAM

"""
Version 1:
"""
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

"""
Version 2:
支持with嵌套
LazyConnection_v2成为专门生产网络连接的工厂类。
"""
class LazyConnection_v2:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()

if __name__ == '__main__':
    from functools import partial

    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)

    conn = LazyConnection_v2(('www.python.org', 80))
    with conn as s1:
        s1.send(b'GET /index.html HTTP/1.0\r\n')
        s1.send(b'Host: www.python.org\r\n')
        s1.send(b'\r\n')
        resp1 = b''.join(iter(partial(s1.recv, 8192), b''))
        print(resp1)
        with conn as s2:
            s2.send(b'GET /index.html HTTP/1.0\r\n')
            s2.send(b'Host: www.python.org\r\n')
            s2.send(b'\r\n')
            resp2 = b''.join(iter(partial(s2.recv, 8192), b''))
            print(resp2)
