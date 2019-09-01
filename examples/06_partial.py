#!/usr/bin/env python
# coding:utf-8

from functools import partial

print(int('10000', base=2))
print(int('10000', base=16))

int2 = partial(int, base=2)
int16 = partial(int, base=16)
print(int2('10000'))
print(int16('10000'))

