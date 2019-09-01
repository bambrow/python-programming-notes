#!/usr/bin/env python
# coding:utf-8


def add(x, y):
    """
    Add two variables.
    :param x:
    :param y:
    :return: the sum of two variables
    """
    return x + y

print(add(3, 4))
to_add = (3, 4)
print(add(*to_add))
ad = add
print(ad("a", "b"))
print(add.__doc__)
print(ad.__name__)
print(ad.__module__)
print("")


def add_end_bad(l=[]):
    l.append('END')
    return l


def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l
print(add_end_bad([1, 2, 3]))
print(add_end_bad())
print(add_end_bad())
print(add_end())
print(add_end())
print("")


def my_fun():
    return 1, 2, 3
a = my_fun()
print(a)
b, c, d = my_fun()
print(b, c, d)
print("")


def my_fun2(a, b, *args):
    print(a, b, args)
my_fun2(1, 2, 3)
my_fun2(1, 2)
my_fun2(1, 2, 3, 4, 5, 6)
print("")


def my_fun3(a, b, *args, **kwargs):
    print(a, b, args)
    print("kwargs:", kwargs)
my_fun3(1, 2)
my_fun3(1, 2, 3, 4, 5)
my_fun3(a = 1, b = 2, c = 3, d = 4)
my_fun3(c = 3, d = 4, a = 1, b = 2)
# my_fun3(1, 2, a = 3, b = 4) // this can cause exception
my_fun3(1, 2, 3, 4, c = 5, d = 6)
print("")


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum
print(calc(1, 2, 3, 4, 5, 6))
lst = [1, 2, 3, 4, 5, 6]
print(calc(*lst))
print("")


def person1(name, age, **kwargs):
    print("name:", name, end=' ')
    print("age:", age, end=' ')
    print("other:", kwargs)
person1("Sam", 15)
person1("Alice", 22, city='New York')
dct = {'city': 'Chicago', 'month': 'August'}
person1("John", 19, **dct)
print("")


# def person2(name, age, *, city):
# def person3(name, age, *args, city):
# in Python 3, we can limit the extra arguments.
# if there is extra argument, it must be city in this case.
# city argument can be None, but name and age are required.
# we must pass in the argument like this: person2('Sam', 15, city='Seattle')


def func(a, b, c=0, *args, **kwargs):
    print("a:", a, "b:", b, "c:", c, "args:", args, "kwargs:", kwargs)
func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 4, 5, 6, d=7, e=8)
tpl = (1, 2, 3, 4, 5)
dct = {'d': 6, 'e': 7}
func(*tpl, **dct)
tpl = (1, 2)
dct = {'c': 3, 'd': 4, 'e': 5}
func(*tpl, **dct)
print("")


def fib(n):
    """
    Calculate Fibonacci number.
    :param n:
    :return: the n-th Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(5))
print(fib(33))  # this will cost some time; recursion is often low in efficiency
print("")


def convert(fun, seq):
    return [fun(i) for i in seq]


def add2(i):
    return i + 2


def mult2(i):
    return i * 2
lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(lst)
lst = convert(add2, lst)
print(lst)
lst = convert(mult2, lst)
print(lst)
print("")


def maker(n):
    def action(x):
        return x ** n
    return action
f = maker(2)
print(f(3))
f = maker(3)
print(f(2))
print("")


def foo(fun):
    def wrap():
        print("wrap starts")
        fun()
        print("wrap ends")
        print(fun.__name__)
    return wrap


@foo
def bar():
    print("this is bar")
bar()
