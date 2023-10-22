#!/usr/bin/env python
# coding:utf-8

import os
import random
import time
from multiprocessing import Process, Queue


def write(q):
    print('Process to write: {0}'.format(os.getpid()))
    for value in ['A','B','C','D','E','F','G','H','I','J','K']:
        print('Put {0} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random() * 2)


def read(q):
    print('Process to read: {0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('Get {0} from queue...'.format(value))

if __name__ == '__main__':
    q = Queue()
    # super process creates Queue and pass to sub processes
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    # start the sub process (read)
    pr.start()
    # start the sub process (write)
    pw.join()
    # wait for pw to finish
    pr.terminate()
    # dead loop, terminate manually
