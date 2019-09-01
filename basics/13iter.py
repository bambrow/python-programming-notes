#!/usr/bin/env python
# coding:utf-8

from collections import Iterable, Iterator

lst = ["a", "b", "c", "d", "e"]
lst_iter = iter(lst)
print(isinstance(lst, Iterable))
print(isinstance(lst, Iterator))
print(isinstance(lst_iter, Iterator))

while True:
    try:
        print(next(lst_iter))
    except:
        print("Error! StopIteration!")
        break
# Python 2: lst_iter.next()
print("\n")

l = (x*x for x in range(10))
print(isinstance(l, Iterable))
print(isinstance(l, Iterator))

while True:
    try:
        print(next(l))
    except:
        print("Error! StopIteration!")
        break
print("\n")

with open("12file.txt") as f:
    print(isinstance(f, Iterable))
    print(isinstance(f, Iterator))
    while True:
        try:
            print(next(f))
        except:
            print("Error! StopIteration!")
            break
print("\n")


def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1

f = fib()
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

for i in range(20):
    print(next(f), end=' ')

print("\n")

for n in fib2(20):
    print(n, end=' ')
