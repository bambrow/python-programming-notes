#!/usr/bin/env python
# coding:utf-8

import re

contents = {}

if __name__ == '__main__':

    with open('cnki_formatter_1.txt', 'r', encoding='utf-8') as fr:
        content_key = ''
        content = ''
        content_year = ''
        for line in fr.readlines():
            line_strip = line.strip()
            if len(line_strip) == 0:
                if len(content_key) > 0:
                    contents.setdefault(content_key, {}).setdefault(content_year, []).append(content)
                    content_key = ''
                    content = ''
                    content_year = ''
                continue
            else:
                if re.match(r'\[\d+\]', line_strip) is not None:
                    content_year = line_strip.split('.')[-2].split(',')[1]
                    # content += line_strip
                else:
                    k, v = re.split(r'\d+', line_strip, maxsplit=1)
                    content_key = k
                    # content += ('\n' + v)

    with open('cnki_formatter_1_result.txt', 'w', encoding='utf-8') as fw:
        for k, vs in contents.items():
            fw.write(k + '\n')
            # fw.write('-'*10 + '\n')
            for kk, vvs in sorted(vs.items()):
                fw.write('(' + kk + '): ' + str(len(vvs)) + '\n')
                # for vv in vvs:
                #     fw.write(vv + '\n')
                # fw.write('\n')
            # fw.write('-'*30 + '\n\n')

