#!/usr/bin/env python
# coding:utf-8


class Chain:

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('{0}/{1}'.format(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

    def __call__(self, username):
        return Chain('{0}/{1}'.format(self._path, username))

print(Chain().user.timeline.recent.post.list)
print('GET', Chain().users('jack').repos)
