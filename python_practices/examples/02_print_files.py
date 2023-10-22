#!/usr/bin/env python
# coding:utf-8

import os


class HandleFiles:

    @staticmethod
    def print_files(path, ignore=True, *, s='..|'):
        for f in os.listdir(path):
            if ignore and f.startswith('.'):
                continue
            p = os.path.join(path, f)
            print(s, end='')
            if os.path.isdir(p):
                print(os.path.relpath(p, path))
                HandleFiles.print_files(p, ignore, s=s+'---')
            else:
                print(os.path.relpath(p, path))

    @staticmethod
    def search_files(path, text, ignore=True):
        for f in os.listdir(path):
            if ignore and f.startswith('.'):
                continue
            p = os.path.join(path, f)
            if text in f:
                print(p)
            if os.path.isdir(p):
                HandleFiles.search_files(p, text, ignore)


if __name__ == '__main__':
    pt = os.path.split(os.path.abspath('.'))[0]
    HandleFiles.print_files(pt)
    HandleFiles.search_files(pt, '01')
