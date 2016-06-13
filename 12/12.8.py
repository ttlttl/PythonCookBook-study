#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
concurrent.futures库中提供了一个ProcessPoolExecutor类，可以用来在单独运行的Python解释器实例中执行计算密集型的函数
"""
import gzip
import io
import glob
from concurrent import futures

def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding="ascii"):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots

def find_all_robots(logdir):
    files = glob.glob(logdir+'/*.log.gz')
    all_robots = set()
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots

if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)