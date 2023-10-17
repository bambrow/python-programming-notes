#!/usr/bin/env python
# coding:utf-8

import sys

# all headers provided by cnki_search_parser
headers_all = ['SrcDatabase-来源库', 'Title-题名', 'Author-作者', 'Organ-单位', 'Source-文献来源', 'Keyword-关键词', 'Summary-摘要',
               'PubTime-发表时间', 'FirstDuty-第一责任人', 'Fund-基金', 'Year-年', 'Period-期', 'Roll-卷', 'PageCount-页码',
               'CLC-中图分类号']
# full headers to be parsed by this script
headers_full = ['SrcDatabase-来源库', 'Title-题名', 'Author-作者', 'Organ-单位', 'Source-文献来源', 'Keyword-关键词', 'PubTime-发表时间',
                'FirstDuty-第一责任人', 'Fund-基金', 'Year-年']
# simplified headers to be parsed by this script
headers = ['来源库', '题名', '作者', '单位', '文献来源', '关键词', '发表时间', '第一责任人', '基金', '年']
# stats flags for each item in headers
headers_stats_flag = [True, False, True, True, True, True, False, True, False, True]
# stats dicts for each item in headers
headers_stats = [{} if x else None for x in headers_stats_flag]
content_cnt = 0


def headers_check():
    assert len(headers) == len(headers_full)
    assert len(headers) == len(headers_stats_flag)
    assert len(headers) == len(headers_stats)


def parse_argv(argv):
    if len(argv) == 1:
        return 'parser_file.txt', True, 20
    if len(argv) == 2:
        return argv[1].strip(), True, 20
    if len(argv) == 3:
        print_stats_flag_parsed = argv[2].lower() == 'print'
        return argv[1].strip(), print_stats_flag_parsed, 20
    if len(argv) == 4:
        print_stats_flag_parsed = argv[2].lower() == 'print'
        stats_user_cnt_parsed = int(argv[3].strip())
        return argv[1].strip(), print_stats_flag_parsed, stats_user_cnt_parsed


def insert_content(line_arg, previous_insertion_arg, last_item_filled_arg):
    if any(header in line_arg for header in headers_full):
        arr = line_arg.split(':', 1)
        header = arr[0].split('-')[1].strip()
        content = arr[1].strip()
        if ';;' in content:
            content_list = content.split(';;')
            content_list_new = [x.strip() for x in content_list if x.strip()]
            content_new = '|'.join(content_list_new)
        elif ';' in content:
            content_list = content.split(';')
            content_list_new = [x.strip() for x in content_list if x.strip()]
            content_new = '|'.join(content_list_new)
        else:
            content_new = content
        i = headers.index(header)
        contents[i] = content_new.replace(',', '，')
        return i, header == headers[-1]
    else:
        if any(header in line_arg for header in headers_all):
            return previous_insertion_arg, last_item_filled_arg
        if ';' == line_arg.strip()[-1]:
            content_new = line_arg.strip().replace(';', '')
        else:
            content_new = line_arg.strip()
        contents[previous_insertion_arg] += ('|' + content_new.replace(',', '，'))
        return previous_insertion_arg, last_item_filled_arg


def populate_stats(contents_arg):
    for i in range(0, len(headers_stats_flag)):
        if headers_stats_flag[i]:
            content = contents_arg[i]
            content_arr = content.split('|')
            for item in content_arr:
                if item.strip():
                    if item.strip() not in headers_stats[i]:
                        headers_stats[i][item.strip()] = 0
                    headers_stats[i][item.strip()] += 1


def print_stats(stats_cnt=-1):
    print("结果总数 = " + str(content_cnt))
    print()
    for i in range(0, len(headers_stats_flag)):
        if headers_stats_flag[i]:
            print('[' + headers[i] + ']' + '统计结果：')
            print('[' + headers[i] + ']' + '计数 = ' + str(len(headers_stats[i])))
            print('[' + headers[i] + ']' + '总频次 = ' + str(sum(headers_stats[i].values())))
            stats_current_cnt = 0
            for k, v in sorted(headers_stats[i].items(), key=lambda item: item[1], reverse=True):
                print(k + ' = ' + str(v))
                stats_current_cnt += 1
                if stats_current_cnt == stats_cnt:
                    break
            print()


def print_grouped_stats():
    for i in range(0, len(headers_stats_flag)):
        if headers_stats_flag[i]:
            print('[' + headers[i] + ']' + '统计结果：')
            grouped_stats = {}
            for k, v in sorted(headers_stats[i].items()):
                grouped_stats.setdefault(v, []).append(k)
            for k, v in sorted(grouped_stats.items(), reverse=True):
                print(str(k) + ' (计数：' + str(len(v)) + ')' + ' = ' + ', '.join(v))
            print()


def save_stats(stats_cnt=-1):
    with open("stats.txt", "w", encoding='utf-8') as f:
        f.write("结果总数 = " + str(content_cnt) + '\n\n')
        for i in range(0, len(headers_stats_flag)):
            if headers_stats_flag[i]:
                f.write('[' + headers[i] + ']' + '统计结果：' + '\n')
                f.write('[' + headers[i] + ']' + '计数 = ' + str(len(headers_stats[i])) + '\n')
                f.write('[' + headers[i] + ']' + '总频次 = ' + str(sum(headers_stats[i].values())) + '\n')
                stats_current_cnt = 0
                for k, v in sorted(headers_stats[i].items(), key=lambda item: item[1], reverse=True):
                    f.write(k + ' = ' + str(v) + '\n')
                    stats_current_cnt += 1
                    if stats_current_cnt == stats_cnt:
                        break
                f.write('\n')


def save_grouped_stats():
    with open('stats_grouped.txt', 'w', encoding='utf-8') as f:
        for i in range(0, len(headers_stats_flag)):
            if headers_stats_flag[i]:
                f.write('[' + headers[i] + ']' + '统计结果：' + '\n')
                grouped_stats = {}
                for k, v in sorted(headers_stats[i].items()):
                    grouped_stats.setdefault(v, []).append(k)
                for k, v in sorted(grouped_stats.items(), reverse=True):
                    f.write(str(k) + ' (计数：' + str(len(v)) + ')' + ' = ' + ', '.join(v) + '\n')
                f.write('\n')


if __name__ == '__main__':
    headers_check()
    input_file, print_stats_flag, stats_user_cnt = parse_argv(sys.argv)
    with open('result.csv', 'w', encoding='utf-8') as fw:
        previous_insertion = -1
        last_item_filled = False
        contents = [''] * len(headers)
        fw.write(','.join(headers) + '\n')
        with open(input_file, 'r', encoding='utf-8') as fr:
            for line in fr.readlines():
                line_strip = line.strip()
                if len(line_strip) == 0:
                    if not all(content == '' for content in contents) and last_item_filled:
                        fw.write(','.join(contents) + '\n')
                        populate_stats(contents)
                        content_cnt = content_cnt + 1
                        contents = [''] * len(headers)
                    continue
                else:
                    previous_insertion, last_item_filled = insert_content(line_strip,
                                                                          previous_insertion,
                                                                          last_item_filled)
    if print_stats_flag:
        print_stats(stats_user_cnt)
        print_grouped_stats()
        # save_stats(stats_user_cnt)
        # save_grouped_stats()
    else:
        save_stats(stats_user_cnt)
        save_grouped_stats()
