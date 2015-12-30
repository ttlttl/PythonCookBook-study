#!/usr/bin/env python
# -*- coding: utf-8 -*-

import html
from html.parser import HTMLParser

s = 'Elements are written as "<tag>text</tag>".'
e = html.escape(s)
print(html.escape(e))
print(html.unescape(e))