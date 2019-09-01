#!/usr/bin/env python
# coding:utf-8

import mysql.connector

with open('dmysql.txt', 'r') as f:
    usr = f.readline().strip()
    passwd = f.readline().strip()

conn = mysql.connector.connect(user=usr, password=passwd, database='test')
cur = conn.cursor()

try:
    cur.execute('drop table user')
finally:
    cur.execute('create table if not exists user (id varchar(20) primary key, name varchar(20))')

try:
    cur.execute('insert into user (id, name) values (%s, %s)', ['1', 'Alice'])
    cur.execute('insert into user (id, name) values (%s, %s)', ['2', 'Bob'])
    cur.execute('insert into user (id, name) values (%s, %s)', ['3', 'Carol'])
    cur.execute('insert into user (id, name) values (%s, %s)', ['4', 'David'])
    cur.execute('insert into user (id, name) values (%s, %s)', ['5', 'Eva'])
    print(cur.rowcount)
    conn.commit()

    cur.execute('delete from user where id=%s', ('5',))
    cur.execute('update user set name=%s where id=%s', ('Dan', '4'))
    conn.commit()

    cur.execute('select * from user where id=%s', ('1',))
    values = cur.fetchall()
    print(values)
    cur.execute('select * from user')
    values = cur.fetchall()
    print(values)
finally:
    cur.close()
    conn.close()
