#!/usr/bin/env python
# coding:utf-8

from wsgiref.simple_server import make_server
from web_development.wsgi.hello import application

httpd = make_server('', 8000, application)
# ip empty
# port 8000
# function application()
print('Serving HTTP on port 8000...')
httpd.serve_forever()

# to test this code
# visit localhost:8000 or localhost:8000/xxx
# ctrl+c to quit
