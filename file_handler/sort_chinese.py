# -*- coding: utf-8 -*-

from pypinyin import pinyin, Style
import sys

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    read_arr = []
    with open(input_file, 'r') as f:
        read_arr = f.readlines()

    en_arr = []
    ch_arr = []
    for i in read_arr:
        if len(i) > 0 and i[0].isascii():
            en_arr.append(i)
        else:
            ch_arr.append(i)
    en_arr.sort(key=str.lower)
    ch_arr.sort(key=lambda keys: [pinyin(i, style=Style.TONE3) for i in keys])
    with open(output_file, 'w') as f:
        f.write(''.join(en_arr))
        f.write(''.join(ch_arr))
