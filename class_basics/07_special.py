#!/usr/bin/env python
# coding:utf-8


class Student:

    def __init__(self, name):
        self._name = name

    # __slots__ = ('_name', '_age', '_score', '_grade')
    # to confine the attributes of this class

    def __len__(self):
        return len(self._name)

    def __str__(self):
        return 'Student: ' + str(self._name)

    __repr__ = __str__

    def __getattr__(self, item):
        if item == 'score':
            return 95
        if item == 'grade':
            return lambda: 'A' # return a function
        raise AttributeError("Student object has no attribute {0}".format(item))

    def __call__(self):
        print('My name is', self._name)

s = Student('Hailey')
print(len(s))
print(s)
print(s.score)
print(s.grade())
s()
print(callable(s))
print(callable(abs))
print()


class Fibs:

    def __init__(self, n):
        self.a, self.b = 0, 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration()
        return self.a

for i in Fibs(3):
    print(i)


class Fib:

    def __init__(self):
        self.a, self.b = 0, 1

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a+b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            negative = False
            if start is None:
                start = 0
            if step is None:
                step = 1
            if step < 0:
                negative = True
                step = -step
            if start < 0 or stop <= 0 or step == 0 or start >= stop or stop is None:
                raise SyntaxError("Illegal slice!")
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x == start:
                    l.append(a)
                    a, b = b, a+b
                    next_one = start + step
                    continue
                if x > start and x == next_one:
                    l.append(a)
                    next_one += step
                a, b = b, a+b
            if not negative:
                return l
            else:
                return list(reversed(l))


f = Fib()
print(f[10])
print(f[5:10])
print(f[:20])
print(f[0:20:2])
print(f[:50:5])
print(f[:50:-5])
