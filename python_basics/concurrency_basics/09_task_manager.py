#!/usr/bin/env python
# coding:utf-8

import queue
import random
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
# the queue to send out tasks
result_queue = queue.Queue()
# the queue to receive results


class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# register two queues to the network
# attribute callable connected to Queue object instances

manager = QueueManager(address=('', 5000), authkey=b'abc')
# port 5000, authkey 'abc'

manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()
# to obtain the Queue object instances of network

for i in range(10):
    # put tasks
    n = random.randint(0, 10000)
    print('Put task {0}...'.format(n))
    task.put(n)

print('Try get results...')
for i in range(10):
    # get results
    try:
        r = result.get(timeout=10)
        print('Result: {0}'.format(r))
    except queue.Empty:
        print('result queue is empty')

manager.shutdown()
print('manager shutdown')

