#!/usr/bin/env python
# coding:utf-8

import asyncio
import threading


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    r = await asyncio.sleep(1)
    # call asyncio.sleep(1) asynchronously
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
# get EventLoop
tasks = [hello(), hello()]
# encapsulate all coroutines
loop.run_until_complete(asyncio.wait(tasks))
# execute coroutine using EventLoop
loop.close()
