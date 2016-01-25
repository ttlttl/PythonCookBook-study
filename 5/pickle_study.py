#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

data = {'name':'ming', 'age':24, 'address':'Shanghai'}

f = open('tmp.tmp', 'wb')
pickle.dump(data, f)
f.close()

f = open('tmp.tmp', 'rb')
data = pickle.load(f)

print(data)