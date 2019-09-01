#!/usr/bin/env python
# coding:utf-8

from collections import OrderedDict


class LIFODict(OrderedDict):

    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        contains_key = 1 if key in self else 0
        if len(self) - contains_key >= self._capacity:
            last = self.popitem(last=True)
            print('remove:', last)
        if contains_key:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

if __name__ == '__main__':
    fd = LIFODict(2)
    fd['a'] = 1
    fd['b'] = 2
    print(fd)
    fd['c'] = 3
    print(fd)
