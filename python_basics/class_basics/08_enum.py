#!/usr/bin/env python
# coding:utf-8

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '->', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Feb = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon)
print(Weekday.Mon.value)
print(Weekday['Mon'])
print(Weekday(1))

for value in Weekday.__members__.items():
    print(value)

for value in Weekday.__members__.values():
    print(value)

for value in Weekday.__members__.values():
    print(value.value)
