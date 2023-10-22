#!/usr/bin/env python
# coding:utf-8


def move(a, b):
    print(a, "->", b)


def hanoi(n, a, b, t):
    if n == 1:
        move(a, b)
    else:
        hanoi(n-1, a, t, b)
        move(a, b)
        hanoi(n-1, t, b, a)

hanoi(4, 'A', 'B', 'C')
