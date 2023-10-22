#!/usr/bin/env python
# coding:utf-8


def _odd_iter():
    n = 3
    while True:
        yield n
        n += 2


def _filter_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    itr = _odd_iter()
    while True:
        n = next(itr)
        yield n
        itr = filter(_filter_divisible(n), itr)

p = primes()

for i in range(10001):
    print(next(p), end=" ")
    if i > 0 and i % 20 == 0:
        print()
