#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
在不同的解释器间进行通信
"""

from multiprocessing.connection import Listener
import traceback

def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')

def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()

if __name__ == '__main__':
    echo_server(('', 25000), authkey=b'peekaboo')
