#!/usr/bin/env python
# coding:utf-8

import hashlib

md5 = hashlib.md5()
md5.update('Hello world!'.encode('utf-8'))
md5.update('I like Beijing Duck'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('Hello world!'.encode('utf-8'))
sha1.update('I like Beijing Duck'.encode('utf-8'))
print(sha1.hexdigest())

# md5 and sha1 are widely used in passwords
