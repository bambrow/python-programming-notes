#!/usr/bin/env python
# coding:utf-8

import asyncio


@asyncio.coroutine
def wget(host):
    print('wget {0}'.format(host))
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: {0}\r\n\r\n'.format(host)
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    # flush buffer
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('{0} header >  {1}'.format(host, line.decode('utf-8').rstrip()))
        # ignore the body
        writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.zhihu.com', 'www.douban.com', 'www.baidu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
