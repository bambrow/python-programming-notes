#!/usr/bin/env python
# coding:utf-8

import os
from multiprocessing import Process


def run_proc(name):
    print('Run child process {0} ({1})...'.format(name, os.getpid()))

if __name__ == '__main__':

    print('Parent process {0}.'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    # target function and arguments
    print('Child process will start.')
    p.start()
    p.join()
    # wait for the child processes to finish, and continue
    print('Child process ends.')
