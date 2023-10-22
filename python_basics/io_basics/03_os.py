#!/usr/bin/env python
# coding:utf-8

import os
import shutil

print(os.name) # posix: Linux, OS X, Unix; nt: windows
print(os.uname()) # detailed system information
print(os.environ) # environment variables
print(os.environ.get('PATH'))

print(os.path.abspath('.')) # absolute path
print(os.path.join(os.path.abspath('.'), 'testdir')) # show the absolute path without actually creating the directory
s = os.path.join(os.path.abspath('.'), 'testdir')
if not os.path.exists(s):
    os.mkdir(s)
else:
    os.rmdir(s)

t = os.path.join(os.path.abspath('.'), 'test.txt')
print(t)
print(os.path.split(t)[-1])
print(os.path.splitext(t)[-1])

if not os.path.isfile('test.txt'):
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write("# This is a text file.")
else:
    if os.path.isfile('test.py'):
        os.remove('test.py')
    os.rename('test.txt', 'test.py')

if os.path.isfile('test.py'):
    shutil.copyfile('test.py', 'test2.py')

print([x for x in os.listdir('.') if os.path.isfile(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[-1] == '.py'])
