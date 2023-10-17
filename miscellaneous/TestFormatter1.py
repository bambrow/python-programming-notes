#!/usr/bin/env python
# coding:utf-8

counts = {}


if __name__ == '__main__':

    with open('test_formatter_1_result.txt', 'w', encoding='utf-8') as fw:
        with open('test_formatter_1.txt', 'r', encoding='utf-8') as fr:
            line_cnt = 0
            for line in fr.readlines():
                line_cnt += 1
                line_strip = line.strip()
                if len(line_strip) > 0:
                    counts.setdefault(line_strip, []).append(str(line_cnt))
                fw.write(str(line_cnt) + ' ' + line)
            fw.write('\n' + '-'*20 + '\n')
            for k, v in counts.items():
                fw.write(k + ': ' + ', '.join(v) + '\n')


