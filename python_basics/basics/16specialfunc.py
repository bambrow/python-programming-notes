#!/usr/bin/env python
# coding:utf-8

from functools import reduce
from operator import add, mul

# lambda
f = lambda x, y: x + 2 * y
print(f(2, 5))
print((lambda x: x ** 2)(6))
lamb = [lambda x: x, lambda x: x**2, lambda x: x**3, lambda x: x**4]
for lam in lamb:
    print(lam(3), end=' ')
print("")
print("")


def add2(i):
    return i + 2

# map
seq = [1, 2, 3, 4, 5, 6, 7, 8]
print(seq)
print(list(map(add2, seq)))
# Python 2: print map(add2, seq)
print(seq)
print([x ** 2 for x in seq])
print("")

seq1 = [1, 2, 3, 4, 5]
seq2 = [6, 7, 8, 9, 10]
seq3 = [11, 12, 13, 14, 15]
seq4 = [16, 17, 18, 19, 20]
print(list(map(lambda i, j, k, l: l + j + k + l, seq1, seq2, seq3, seq4)))
print("")

# reduce
print(reduce(lambda x, y: x + y, seq))
print(reduce(lambda x, y: x + y, seq, 1))
print(reduce(lambda x, y: x + y, seq, 2))
print("")

# compute seq1[0]seq2[0] + ... + seq1[n]seq2
# answer 1
print(list(zip(seq1, seq2)))
print(sum(x*y for x,y in zip(seq1, seq2)))
# answer 2
print(reduce(add, list(map(mul, seq1, seq2))))
# answer 3
print(reduce(lambda x, y: x+y, list(map(lambda x, y: x*y, seq1, seq2))))
print("")

# filter
# [item for item in iterable if function(item)]
# or [item for item in iterable if item]
print([x for x in seq if x > 3])
print([x for x in 'elementary' if x != 'e'])
print([s for s in ['a', '', 'b', '', None, 'c', '   '] if s and s.strip()])
# Python 2: print filter(...)
print("")

# zip
# make an iterator that aggregates elements from each of the iterables
# returns an iterator of tuples
# Python 2: zip(*iterables)
print(list(zip(seq1, seq2, seq3, seq4)))
matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
print(matrix)
print(list(zip(*matrix)))
seq = list(range(1, 10))
print(list(zip(*[iter(seq)]*3)))
print("")

# sorted
lst = [5, -7, 2, -6, 3]
print(lst)
print(sorted(lst))
print(sorted(lst, key=abs))
lst = ['a', 'B', 'c', 'D']
print(sorted(lst))
print(sorted(lst, key=str.lower))

