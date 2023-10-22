#!/usr/bin/env python
# coding:utf-8

import fileinput
import os
import time

f = open("12file.txt")
print(f.name)
print(f.mode)
print(f.closed)
for line in f:
    print(line, end=' ')
f.close()
print("\n")

f = open("12file.txt")
for line in f:
    print(line.strip())
f.close()
print("\n")

nf = open("12file2.txt", "w")
nf.write("This is a file.")
nf.close()

# The following modes are supported:
# r read
# w write (if file exists, clear the file first; if file does not exist, create the file)
# a append (if file does not exist, create the file)
# r+ read and write
# w+ read and write, but clear the file first
# a+ read and write, but from the end of the file

# this method does not require the file.close()
with open("12file.txt") as f:
    print(f.read())
print("\n")

with open("12file.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end=' ')
print("\n")

with open("12file.txt") as f:
    lines = f.readlines()
    print(lines)
    print("".join(lines))
print("\n")

file_stat = os.stat("12file.txt")
print(time.localtime(file_stat.st_ctime))
print("\n")

# use module fileinput
for line in fileinput.input("12file.txt"):
    print(line, end=' ')
print("\n")

f = open("12file.txt")
print(f.readline(), end=' ')
f.seek(0)
print(f.readline(), end=' ')
print(f.tell())
f.seek(7)
print(f.readline(), end=' ')
# f.seek(-5, 1)
# print(f.readline(), end=' ')
# f.seek(-15, 2)
# print(f.readline(), end=' ')
f.close()
