#!/usr/bin/env python
# coding:utf-8

import functools, time


def log(text):
    def decorator(func):
        @functools.wraps(func) # to avoid func.__name__ change to wrapper
        def wrapper(*args, **kwargs):
            print('{0} {1}():'.format(text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log('execute')
def now():
    print(time.time())

now()
