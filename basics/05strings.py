#!/usr/bin/env python
# coding:utf-8

print(dir(str))

s = "Welcome to Python world!"
s2 = "Welcome To Python World!"
t = "HELLO"
t2 = "hello"
u = "123"

print(t.isalpha())
print(u.isdigit())
print(s.istitle())
print(s2.istitle())
print(t.istitle())
print(s.title())
print("\n")

print(t.isupper())
print(t2.islower())
print(s.capitalize())
print(t.capitalize())
print(t2.capitalize())
print("\n")

print(s.upper().isupper())
print(s.lower().islower())
print(s.title().istitle())
print("\n")

print(s.split(" "))
print(s.split(" ", 1))
print(s.split(" ", 2))
print(s.split("o"))
print("\n")

a = s.split(" ")
print(".".join(a))
print("-".join(a))
print("\n")

test = "ABCDEABCDEABCDE"
print(test)
print(test.replace("A", "*"))
print(test.replace("A", "*", 1))
print(test.replace("A", "*", 2))
print(test.find("B"))
print(test.find("B", 2))
print(test.find("B", 7, 10))
print(test.rfind("B"))
print(test.rfind("B", 2))
print(test.rfind("B", 7, 10))
print("\n")

print(test.index("BC"))
print(test.index("BC", 2))
print(test.index("BC", 8, 13))
print(test.rindex("BC"))
print(test.rindex("BC", 2))
print(test.rindex("BC", 8, 13))
print("\n")

print(s.startswith("we"))
print(s.startswith("We"))
print(s.endswith("e!"))
print("\n")

print(s.center(40))
print(s.center(40, "-"))
print(s.center(40, "*"))
print(s.ljust(40, "-"))
print(s.rjust(40, "-"))
print("\n")
