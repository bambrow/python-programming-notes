#!/usr/bin/env python
# coding:utf-8

s = "123456789"
print(s)
print("".join(list(reversed(s))))
print("\n")

s = "579124863"
print(s)
print(", ".join(sorted(list(reversed(s)), reverse=True)))
print("\n")

s = "12\n34\t5       67 89"
print(s.split())
print(s.split(" ", 3))
print("\n")

s = "123456789"
print(s)
a = list(reversed(s))
a.reverse()
print(a)
a = [int(i) for i in a]
print(a)
print([i**2 for i in a])
print("\n")

b = list(enumerate([i**2 for i in a]))
print(b)
foo = lambda j, k: "%d: %d"%(j+1, k)
print([foo(j, k) for j, k in enumerate([i**2 for i in a])])
print("\n")

c = ["  a", "b     ", " c   ", "   d "]
print(c)
print([one.strip() for one in c])
print(tuple(a))
print(list(tuple(a)))
print("\n")

d = 1, 2, 3, 6, 7
print(d)
print(d[4])
print(tuple([i+3 for i in d]))
