#!/usr/bin/env python
# coding:utf-8

import itertools

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

cs = itertools.cycle('ABC')
i = 0;
for c in cs:
    print(c, end=' ')
    i += 1
    if i == 10: break

print()

cs = itertools.repeat('ABC', 3)
for c in cs:
    print(c, end=' ')

print()

for c in itertools.chain('ABC', 'XYZ'):
    print(c, end=' ')

print()

for key, group in itertools.groupby('aAbbBcCaa', lambda c: c.upper()):
    print(key, list(group))


