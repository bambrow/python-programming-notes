#!/usr/bin/env python
# coding:utf-8

a = []
print(type(a))
print(bool(a))
print(a)
print("\n")

a = ["a", "b", "c", 1, 2, 3, "Hello"]
print(bool(a))
print(len(a))
print(a[0])
print(a[-1])
print(a[2:4])
print("\n")

print(a[-3:-1])
print(a[2:])
print(a[:4])
print(a[1:5:2])
print(a[:5:3])
print("\n")

print(a[1::3])
print(a[-1][2:4])
print(a[-1][::2])
print(a[-2::1])
print(a[-2::-1])
print("\n")

print(a[-2::-2])
print(a[-2:0:-1])
print(a[-2:0:-2])
b = a[:]
print(b)
print(id(a))
print(id(b))
print("\n")

print(a.index(1))
a.append(1)
a.append(2)
a.append(4)
print(a)
print(a.index(1))
print(a[::-1])
print(list(reversed(a)))
# a.sort(reverse=True)
print(a)
a.reverse()
print(a)
print(hasattr(a, '__iter__'))
print("\n")

s = "abcdefg"
print(s)
print("".join(list(reversed(s))))
print("\n")

print(a + a)
print(a * 2)
print("a" in a)
print(1 in a)
# print(max(a))
# print(min(a))
print("\n")

b = ["q", "w", "e", "r"]
print(id(a))
a.extend(b)
print(a)
print(id(a))
a.extend(s)
print(a)
print(id(a))
print("\n")

print(a.count("a"))
print(a.count(100))
a.insert(1, 100)
print(a)
print(a.count(100))
print("\n")

print(a.pop())
print(a.pop(9))
print(a)
a.remove("d")
print(a)
a.remove("a")
print(a)

