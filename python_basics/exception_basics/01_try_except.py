#!/usr/bin/env python
# coding:utf-8

import logging


def func(a):
    try:
        print('try...')
        r = 10 / int(a)
        print('result:', r)
    except ValueError as e:
        logging.exception(e)
    except ZeroDivisionError as e:
        logging.exception(e)
    else:
        print('no error...')
    finally:
        print('finally...')

func(1)
func(0)
func('a')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError("Invalid value: {0}".format(n))
    return n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print("ValueError!")
        raise

bar()
