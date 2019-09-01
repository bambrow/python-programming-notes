#!/usr/bin/env python
# coding:utf-8

import random

ints = [random.randint(0, 100) for i in range(50)]
print(ints)
ave = sum(ints) / len(ints)
ints_below_ave = [i for i in ints if i < ave]
print(ints_below_ave)
print("\n")

s = "Hello    world!   I love   Python       !"
print(s)
s_list = s.split(" ")
print(s_list)
s_list_strip = [word for word in s_list if word != '']
print(s_list_strip)
print(" ".join(s_list_strip))
print("\n")

a, b = 0, 1
for i in range(100):
    a, b = b, a + b
print(a)
print("\n")
