#!/usr/bin/env python
# coding:utf-8

import base64

be = base64.b64encode(b'binary string')
print(be)

bd = base64.b64decode(be)
print(bd)
print(bd.decode('utf-8'))

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))


