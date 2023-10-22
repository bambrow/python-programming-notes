#!/usr/bin/env python
# coding:utf-8

import os

print('Process {0} start...'.format(os.getpid()))
pid = os.fork()
if pid == 0:
    print('Child process ({0}) and parent is {1}...'.format(os.getpid(), os.getppid()))
else:
    print('({0}) created child process {1}...'.format(os.getpid(), pid))

