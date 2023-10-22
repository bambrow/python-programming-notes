#!/usr/bin/env python
# coding:utf-8

import asyncio
import threading


@asyncio.coroutine # label a generator as coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    r = yield from asyncio.sleep(1)
    # call asyncio.sleep(1) asynchronously
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
# get EventLoop
tasks = [hello(), hello()]
# encapsulate all coroutines
loop.run_until_complete(asyncio.wait(tasks))
# execute coroutine using EventLoop
loop.close()

# yield and yield from
# example:
#
# def g1(x):
#   for i in range(x):
#       yield i
#
# def g2(x):
#   yield from range(x)
#
# g1(5) and g2(5) generate the same results
#
#
# yield from will use the embedded output of generator as part of the current generator
# example:
#
# def g(x):
#   yield from range(x, 0, -1)
#   yield from range(x)
#
# list(g(5))
# [5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
#

