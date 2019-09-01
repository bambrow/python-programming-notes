#!/usr/bin/env python
# coding:utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
# connect to the server
# the argument is a tuple

print(s.recv(1024).decode('utf-8'))
# print welcome message

for data in [b'Alice', b'Bob', b'Cate', b'David']:
    s.send(data)
    # send data
    print(s.recv(1024).decode('utf-8'))
    # print the feedback message

s.send(b'exit')
s.close()
