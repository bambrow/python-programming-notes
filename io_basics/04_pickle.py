#!/usr/bin/env python
# coding:utf-8

import pickle

d = dict(name='Hailey', age=21, score=95)
print(pickle.dumps(d))
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as f:
    d2 = pickle.load(f)
print(d2)
