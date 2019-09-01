#!/usr/bin/env python
# coding:utf-8

from collections import Iterable

a = [1, 4, 5, 2, 8]
b = [8, 3, 4, 2, 6, 7, 9]

length = len(a) if len(a) < len(b) else len(b)
print(length)

c = []
for i,j in zip(a, b):
    c.append(i + j)

print(c)

matrix = [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)]
print(list(zip(*matrix)))

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for (i, day) in enumerate(week, start=1):
    print(str(i) + ": " + day, end=' ')
print("\n")

print([i+j for i in 'ABC' for j in 'XYZ'])
print("\n")

print(isinstance('abc', Iterable))
print(isinstance(week, Iterable))
print(isinstance(123, Iterable))
print("\n")
