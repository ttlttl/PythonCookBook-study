#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii

s = b'hello'
print(s)
h = binascii.b2a_hex(s)

print(h)

print(binascii.a2b_hex(h))