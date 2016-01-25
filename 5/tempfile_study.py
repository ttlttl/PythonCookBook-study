#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
    f.write('hello, world')
    f.write('Testing\n')

    f.seek(0)
    data = f.read()
    print(data)
