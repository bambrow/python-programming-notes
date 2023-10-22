#!/usr/bin/env python
# coding:utf-8


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

# environ: a dict containing all HTTP request information
# start_response: a function sending HTTP response
# start_response('200 OK', [('Content-Type', 'text/html')]) send out the Header of response
#     param: response code, a list of HTTP Header containing tuples
# return the HTTP Body
