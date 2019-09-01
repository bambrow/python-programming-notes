#!/usr/bin/env python
# coding:utf-8

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

while True:
    data, addr = s.recvfrom(1024)
    time.sleep(1)
    if not data or data.decode('utf-8') == 'exit':
        break
    s.sendto(('Hello, {0}'.format(data.decode('utf-8'))).encode('utf-8'), addr)
