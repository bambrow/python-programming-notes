#!/usr/bin/env python
# coding:utf-8

from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# create base class


class User(Base):

    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

with open('dmysql.txt', 'r') as f:
    usr = f.readline().strip()
    passwd = f.readline().strip()

engine = create_engine('mysql+mysqlconnector://%s:%s@localhost:3306/test' % (usr, passwd))
# initialize database connection
DBSession = sessionmaker(bind=engine)
# create DBSession class
session = DBSession()
# create session

# user = session.query(User).filter(User.id=='5').one()
# session.delete(user)

try:
    new_user = User(id='5', name='Eva')
    # create a new user
    session.add(new_user)
    # add to session
    session.commit()
    # commit the change
    user = session.query(User).filter(User.id=='5').one()
    # create query, filter is equal to where
    # one() returns one line, all() returns all lines
    print(user.id + ' ' + user.name)
    session.delete(user)
    # delete the user
    session.commit()
finally:
    session.close()


