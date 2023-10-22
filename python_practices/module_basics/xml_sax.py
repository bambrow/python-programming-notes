#!/usr/bin/env python
# coding:utf-8

from xml.parsers.expat import ParserCreate


class SaxHandler:

    def start_element(self, name, attrs):
        print('sax:start_element: {0}, attrs: {1}'.format(name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: {0}'.format(name))

    def char_data(self, text):
        print('sax:char_data: {0}'.format(text))

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = SaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
