#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
使用with语句创建一个上下文环境，当程序的控制流程离开with语句块后，文件将自动关闭。
使用newline=''参数，Python不会将'\n'或'\r\n'自动转换为当前系统默认的换行符。
使用encoding指定编码方式。
使用errors='ignore'或'replace'指定编码错误的处理方式。
生命苦短，使用utf-8！！！
"""
with open(__file__, 'rt', newline='',encoding='ascii', errors='ignore') as f:
    print(f.read())
