#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
用函数代替只有单个方法的类。
只有单个方法的类可以通过闭包将其转换成函数。
"""

from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM, APPL, FB', fields='sllclv'):
    print(line.decode('utf-8'))


"""
使用嵌套函数或者说闭包常常会显得更加优雅，简单来说闭包就是一个函数，还保存着额外的环境变量。
闭包的核心特性是它可以记住定义闭包时的环境。
在编写的代码中需要附加额外的状态给函数时，考虑使用闭包。
"""
def urltemplate(template):
    def operner(**kwargs):
        return urlopen(template.format_map(kwargs))
    return operner

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,APPL,FB', fields='sllclv'):
    print(line.decode('utf-8'))