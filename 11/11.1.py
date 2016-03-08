"""
以客户端的形式同HTTP服务交互
"""

from urllib import request, parse

url = 'http://httpbin.org/get'

parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

querystring = parse.urlencode(parms)

#http get
u = request.urlopen(url + '?' + querystring)
print(u.read())

#post
u = request.urlopen(url, querystring.encode('ascii'))
print(u.read())
