#!/usr/bin/env python
# coding:utf-8

import logging
logging.basicConfig(level=logging.INFO)
# level: INFO, DEBUG, WARNING, ERROR


def foo(s):
    n = int(s)
    logging.info('n = {0}'.format(n))
    assert n != 0, 'n is zero!'
    return 10 / n


def bar():
    try:
        foo('0')
    except AssertionError:
        print("AssertionError!")

bar()

