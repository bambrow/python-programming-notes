import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    pd_all = pd.read_csv('info.csv', sep=',', encoding='utf-8')
    pd_all.book_timestamp = pd_all.apply(lambda x: date_format(x.book_timestamp), axis=1)
    pd_all.modify_timestamp = pd_all.apply(lambda x: date_format(x.modify_timestamp), axis=1)
    pd_all.to_csv('result.csv', sep='\t', index=False, encoding='utf-8')


def date_format(x):
    if not isinstance(x, str):
        return x
    time = datetime.strptime(x, '%d/%m/%Y %H:%M:%S')
    return time.strftime('%Y-%m-%d %H:%M:%S')
