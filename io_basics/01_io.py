#!/usr/bin/env python
# coding:utf-8


with open('example.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f.readlines():
        print(line.strip())

with open('example2.txt', 'w', encoding='utf8') as f:
    f.write('Hello World!')