#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建一个TCP服务器
"""

from socketserver import BaseRequestHandler, TCPServer

#定义处理类，实现了一个handle()方法来服务于客户端的连接。
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

from socketserver import StreamRequestHandler

class EchoHandlerV2(StreamRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        for line in self.rfile:
            self.wfile(line)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()
