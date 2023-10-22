#!/usr/bin/env python
# coding:utf-8

import re

if __name__ == '__main__':

    with open('bccwj_formatter_1.txt', 'r', encoding='utf-8') as fr:
        with open('bccwj_formatter_1_result.txt', 'w', encoding='utf-8') as fw:
            for line in fr.readlines():
                line_strip = line.strip()
                


