#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建一个UDP服务器
"""

from socketserver import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 2000), TimeHandler)
    serv.serve_forever()
