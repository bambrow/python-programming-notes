#!/usr/bin/env python
# coding:utf-8

import os
import sqlite3

if os.path.isfile('dsqlite.db'):
    os.remove('dsqlite.db')
# remove the database file if already exists

conn = sqlite3.connect('dsqlite.db')
# connect the database
# if does not exist, create one
cur = conn.cursor()
# create a cursor
cur.execute('create table user (id varchar(20) primary key, name varchar(20))')
# create a table
cur.execute('insert into user (id, name) values (\'1\', \'Alice\')')
cur.execute('insert into user (id, name) values (\'2\', \'Bob\')')
cur.execute('insert into user (id, name) values (\'3\', \'Carol\')')
cur.execute('insert into user (id, name) values (\'4\', \'David\')')
cur.execute('insert into user (id, name) values (\'5\', \'Eva\')')
# insert rows
print(cur.rowcount)
# print the row number
conn.commit()
# commit the change

cur.execute('delete from user where id=?', ('5',))
cur.execute('update user set name=? where id=?', ('Dan', '4'))
conn.commit()

cur.execute('select * from user where id=?', ('1',))
# do the search
values = cur.fetchall()
print(values)
cur.execute('select * from user')
values = cur.fetchall()
print(values)
cur.close()
conn.close()
# close the cursor and connection
