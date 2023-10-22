#!/usr/bin/env python
# coding:utf-8

import threading
import time

b = 0
lock = threading.Lock()


def change(x):
    global b
    b += x
    b -= x


def run(x):
    start = time.time()
    for i in range(1000000):
        change(x)
    end = time.time()
    print('Running time: {0:.2f}'.format(end-start))

t1 = threading.Thread(target=run, args=(2,))
t2 = threading.Thread(target=run, args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print(b)

b = 0


def run_with_lock(x):
    start = time.time()
    for i in range(1000000):
        lock.acquire()
        try:
            change(x)
        finally:
            lock.release()
    end = time.time()
    print('Running time: {0:.2f}'.format(end-start))

t3 = threading.Thread(target=run_with_lock, args=(2,))
t4 = threading.Thread(target=run_with_lock, args=(3,))
t3.start()
t4.start()
t3.join()
t4.join()
print(b)
