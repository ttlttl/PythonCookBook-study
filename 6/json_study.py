#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pprint
object_pairs_hook
object_hook
indent
sort_keys
"""
from urllib.request import urlopen, Request
import json
from pprint import pprint

url = 'http://apis.baidu.com/heweather/weather/free?city=shanghai'
req = Request(url)
req.add_header("apikey", "ebfc3a7186254a37fc715d2f9d4c4049")
resp = urlopen(req)
content = resp.read().decode('utf-8')
j = json.loads(content)
pprint(j)

print('*-' * 10)


from collections import OrderedDict
s = '{"name":"ACME", "shares":50, "price":490.1}'

#object_pairs_hook
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)
print("*-" * 10)

#indent, sort_keys
print(json.dumps(data, indent=4, sort_keys=True))
print("*-" * 10)


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

#object_hook
data = json.loads(s, object_hook=JSONObject)
print(data.name)


#class instance to json
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = {'__classname__' : type(obj).__name__}
    d.update(vars(obj))
    return d

classes = {
    'Point' : Point
}

def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for k, v in d.items():
            setattr(obj, k, v)
            return obj
    else:
        return d

p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s)
a = json.loads(s, object_hook=unserialize_object)
print(a.x)



