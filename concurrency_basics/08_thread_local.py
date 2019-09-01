#!/usr/bin/env python
# coding:utf-8

import threading

local_school = threading.local()
# create ThreadLocal object instance
# ThreadLocal is a useful tool to make sure that each thread has its own local variable,
#   and different threads' local variables do not influence each other.


def process_student():
    # to get the student attribute associated with current thread (from ThreadLocal)
    std = local_school.student
    print('Hello, {0} (in {1})'.format(std, threading.current_thread().name))


def process_thread(name):
    # to set the student attribute associated with current thread (to ThreadLocal)
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Hailey',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Jack',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


