#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gzip
import bz2

with gzip.open('tmp.gz', 'at', compresslevel=9) as f:
    f.write('hello, gzip\n')

with gzip.open('tmp.gz', 'rt') as f:
    print(f.read())

with bz2.open('tmp.bz2', 'at', compresslevel=9) as f:
    f.write('hello, bz2\n')

with bz2.open('tmp.bz2', 'rt') as f:
    print(f.read())