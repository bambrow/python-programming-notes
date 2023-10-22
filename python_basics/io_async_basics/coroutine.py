#!/usr/bin/env python
# coding:utf-8


def consumer():
    # a generator which implements coroutine
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    # initiate the generator, r = '', pause at yield r
    n = 0
    while n < 10:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        # send n into generator, n = 1 for the first run, and r = '200 OK'
        # pause at yield r again, and return the value ('200 OK') to r
        # wait for the next send, which is another loop in this function
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()
    # close the function

c = consumer()
produce(c)
