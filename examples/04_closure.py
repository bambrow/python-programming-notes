#!/usr/bin/env python
# coding:utf-8


def count(n):
    f = lambda j: lambda: j*j
    lst = []
    for i in range(1, n):
        lst.append(f(i))
    return lst

lst = count(10)

for f in lst:
    print(f(), end=" ")
