#!/usr/bin/env python
# coding:utf-8

global x


def func(x):
    x += 2

x = 5
print(x)
func(x)
print(x)


def print_locals(a, b):
    c = 'in the function'
    print(locals())

print_locals(1, 'hello')

print(globals())
print(globals()['x'])
