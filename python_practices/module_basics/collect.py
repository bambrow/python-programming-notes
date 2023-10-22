#!/usr/bin/env python
# coding:utf-8

from collections import *

# namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(2, 3)
print(p.x, p.y)

# deque

q = deque(['a', 'b', 'c'])
q.append('d')
q.append('e')
print(q)
q.pop()
q.popleft()
print(q)

# defaultdict

dd = defaultdict(lambda: 'N/A')
dd['k1'] = 'a'
dd['k2'] = 'b'
print(dd['k1'], dd['k2'], dd['k3'])

# OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('z', 4), ('x', 5), ('y', 6)])
d = dict([('a', 1), ('b', 2), ('c', 3), ('z', 4), ('x', 5), ('y', 6)])
print(d, od)

# Counter

c = Counter()
for ch in 'entertainment':
    c[ch] += 1
print(c)

'''
data types in collections module

namedtuple()	factory function for creating tuple subclasses with named fields
deque	list-like container with fast appends and pops on either end
ChainMap	dict-like class for creating a single view of multiple mappings
Counter	dict subclass for counting hashable objects
OrderedDict	dict subclass that remembers the order entries were added
defaultdict	dict subclass that calls a factory function to supply missing values
UserDict	wrapper around dictionary objects for easier dict subclassing
UserList	wrapper around list objects for easier list subclassing
UserString	wrapper around string objects for easier string subclassing
'''