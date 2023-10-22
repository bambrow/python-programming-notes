#!/usr/bin/env python
# coding:utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create a socket
# AF_INET: IPv4
# AF_INET6: IPv6
# SOCK_STREAM: TCP
s.connect(('daily.zhihu.com', 80))
# create connection
# 80: HTTP
# 25: SMTP
# 21: FTP
# port number smaller than 1024: Internet standard service port
# port number greater than 1024: use freely

s.send(b'GET / HTTP/1.1\r\nHost: daily.zhihu.com\r\nConnection: close\r\n\r\n')
# send request for returning the front page
# HTTP protocol: client must send request to server first
#   after server receives the request, it will return the data

buffer = []
# create a buffer
while True:
    d = s.recv(1024)
    # receive at most 1024 bytes at a time
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()
# close the socket

header, html = data.split(b'\r\n\r\n', 1)
# split the header and the html
print(header.decode('utf-8'))
with open('tcp.html', 'wb') as f:
    f.write(html)
# write the html to a file
