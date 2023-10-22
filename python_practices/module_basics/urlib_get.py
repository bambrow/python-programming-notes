#!/usr/bin/env python
# coding:utf-8

from urllib import request

with request.urlopen('http://news-at.zhihu.com/api/4/news/latest') as f:
    # Zhihu Daily newest feed API
    data = f.read()
    print('Status:', f.status, f.reason)
    print()
    for k, v in f.getheaders():
        print('{0}: {1}'.format(k, v))
    print("################################################################")
    print('Data:', data.decode('utf-8'))

print("################################################################")

req = request.Request('http://daily.zhihu.com/')
# Zhihu Daily frontpage
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# add header; request for iPhone version page
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('{0}: {1}'.format(k, v))
    print("################################################################")
    print('Data:', f.read().decode('utf-8'))

