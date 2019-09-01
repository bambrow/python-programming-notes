#!/usr/bin/env python
# coding:utf-8

from types import MethodType


class Student():
    __slots__ = ('age', 'set_age')
    # confine the available attributes
    # not working for subclasses, unless __slots__ defined in subclasses


def set_age(self, age):
    self.age = age

s = Student()
s.set_age = MethodType(set_age, s)
s.set_age(21)
print(s.age)

s2 = Student()
print(hasattr(s2, 'age'))

Student.set_age = set_age
s2.set_age(20)
print(s2.age)

