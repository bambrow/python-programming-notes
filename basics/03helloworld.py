#!/usr/bin/env python
# coding:utf-8

"""
This is the head file.
"""

# this is a comment.

print("Hello world!")
print("What's your name?")
print("Well... \"Bambrow...?\"")
print("Hello, " + "Bambrow!")
print()

a = 147

print(str(a) + " is a number.")
print(repr(a) + " is a number.")
print()

print("""
Print...
...as many as you want.
""")
print()

print("\' \" \\ \n \t escape character.")
print(r"\' \" \\ \n \t original string.")
print()

b = "number"
print("%d is a %s" % (a, b))
print(b * 8)
print("i" in b)
print(min(b))
print(max(b))
print()

print(help(input))
print()

name = input("Input your name:")
# Python 2: use raw_input instead of input
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.istitle())
print(name.isupper())
print(name.islower())
# input always returns a string
print()

s = "Another test!"
print(s)
print(s[0])
print(s[-1])
print(s[2:5])
print(s[2:])
print(s[:5])
print(s[:])
print()

s2 = s[:]
print(id(s))
print(id(s2))
print(s > s2)
# Python 2: cmp(s, s2)
print()

t = "     Need striping.    "
print(t)
print(t.strip())
print(t.lstrip())
print(t.rstrip())
print()
