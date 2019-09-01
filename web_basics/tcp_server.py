#!/usr/bin/env python
# coding:utf-8

import socket, threading, time


def tcplink(sock, addr):
    print('Accept new connection from {0}:{1}'.format(addr[0], addr[1]))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, {0}'.format(data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print("Connection from {0}:{1} is now closed.".format(addr[0], addr[1]))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
# 0.0.0.0 all network addresses
# 127.0.0.1 localhost
# port number 9999
# the argument is a tuple

s.listen(5)
# monitor the port
# maximum number of connections: 5
print('Waiting for connection...')

while True:
    sock, addr = s.accept()
    # accept a new connection
    t = threading.Thread(target=tcplink, args=(sock, addr))
    # create a new thread for a new connection
    t.start()

