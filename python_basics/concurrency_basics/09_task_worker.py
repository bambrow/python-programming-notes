#!/usr/bin/env python
# coding:utf-8

import queue
import sys
import time
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# to obtain the Queue object instances from network

server_addr = '127.0.0.1'
print('Connect to server {0}...'.format(server_addr))
# connect to the server where manager is in

m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
try:
    m.connect()
except:
    print('manager offline')
    sys.exit('exit...')

task = m.get_task_queue()
result = m.get_result_queue()
# get Queue object instances

for i in range(10):
    # get tasks from Queue
    try:
        n = task.get(timeout=1)
        print('run task {0} * {0}...'.format(n))
        r = '{0} * {0} = {1}'.format(n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty')

print('worker shutdown')

