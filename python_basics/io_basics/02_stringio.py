#!/usr/bin/env python
# coding:utf-8

from io import StringIO, BytesIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')
f.write('!')
print(f.getvalue())

f = StringIO('1\n2\n3\n4\n5\n6')
while True:
    s = f.readline()
    if s == '': break
    print(s.strip())

f = BytesIO()
f.write('蛤蛤蛤'.encode('utf-8'))
print(f.getvalue())

