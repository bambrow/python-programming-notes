#!/usr/bin/env python
# coding:utf-8

import sys

print(sys.getdefaultencoding())

print(ord("a"))
print(ord("A"))
print(chr(97))
print(chr(65))
print("\n")

print(help(ord))
print(help(chr))
print("\n")

s = "蛤"
print(s)
print(len(s))
print(ord(s))
print(type(s))
print("\n")

print(help(str.encode))
# print(help(str.decode))
print("\n")

# Python 3 does not have decode method

t = s.encode("utf-8")
print(type(t))
print(len(t))
print(t)
print(len(t.decode("utf-8")))
print(t.decode("utf-8"))
print("\n")

# if you want to use Chinese in Python:
# solution 1: make statement at the beginning (coding:utf-8)

# solution 2: transfer to Unicode
unicode_str = str('中文')
# Python 2: unicode_str = str('中文', encoding='utf-8')
print(unicode_str.encode('utf-8'))

# solution 3: use 'u' when creating a string
unicode_str = "中文"
print(unicode_str)

# solution 4: use codecs.open instead of open
# import codecs
# codecs.open('filename', encoding='utf8')
