#!/usr/bin/env python
# coding:utf-8

import types

print(type(1))
print(type('a'))
print(type(abs))


def func():
    pass

print(type(1)==int)
print(type('a')==str)
print(type(func)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(5)))==types.GeneratorType)

print(isinstance(1, int))
print(isinstance('a', str))
print(isinstance([1, 2, 3], list))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


class MyObject():

    def __init__(self):
        self.a = 5

    def add2(self):
        return self.a + 2

a = MyObject()
print(dir(a))
print(hasattr(a, 'a'))
print(hasattr(a, 'x'))
setattr(a, 'x', 1)
print(hasattr(a, 'x'))
print(getattr(a, 'x'))
print(getattr(a, 'y', 404))
print(hasattr(a, 'add2'))
fn = getattr(a, 'add2')
print(fn())

