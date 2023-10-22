#!/usr/bin/env python
# coding:utf-8

print(help(str.format))

print("I like {0} and {1}".format("Python", "Java"))
print("I like {1} and {0}".format("Python", "Java"))
print()

print("I like {0:10} and {1:>15}".format("Python", "Java"))
print("I like {0:^10} and {1:^15}".format("Python", "Java"))
print()

print("I like {0:^5.2} and {1:^10.3}".format("Python", "Java"))
print()

print("I am {0:4d} years old and I am {1:^6.2f}m tall.".format(22, 1.789382773))
print("I am {0:4d} years old and I am {1:06.2f}m tall.".format(22, 1.789382773))
print()

print("I am {age} years old and I am {height}m tall.".format(age=22, height=1.789382773))
print()

data = {"age": 22, "height": 1.789382773}
print("I am {age} years old and I am {height}m tall.".format(**data))
