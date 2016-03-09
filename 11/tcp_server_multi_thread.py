#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socketserver import StreamRequestHandler, TCPServer
from threading import Thread

class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from ', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)

if __name__ == '__main__':
    NWORKERS = 16
    serv = TCPServer(('', 20001), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.demon = True
        t.start()
    serv.serve_forever()