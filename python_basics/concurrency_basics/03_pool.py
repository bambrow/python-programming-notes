#!/usr/bin/env python
# coding:utf-8

import os
import random
import time
from multiprocessing import Pool


def long_time_task(name):
    print('Run task {0} ({1})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {0} runs {1:.2f} seconds.'.format(name, end-start))

if __name__ == '__main__':

    n = 5
    print('Parent process {0}.'.format(os.getpid()))
    p = Pool(5)
    # maximum child processes number is 5
    for i in range(10):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all child processes done...')
    p.close()
    # required before p.join(): stop adding new processes
    p.join()
    # wait for the child processes to finish, and continue
    print('All child processes done.')
