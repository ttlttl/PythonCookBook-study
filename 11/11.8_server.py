#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
实现远程过程调用
"""

import pickle

class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, connection):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(connection.recv())
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass


from multiprocessing.connection import Listener
from threading import Thread

def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

if __name__ == '__main__':
    handler = RPCHandler()
    handler.register_function(add)
    handler.register_function(sub)

    rpc_server(handler, ('localhost', 17000), authkey=b'peekaboo')