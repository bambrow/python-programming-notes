#!/usr/bin/env python
# coding:utf-8

import hashlib, random


class User:

    def __init__(self):
        self.__usrname = None
        self.__md5 = None
        self.__log_in = False
        self.__new = True

    def __calc_md5(self, username, password):
        md5 = hashlib.md5()
        md5.update(username.encode('utf-8'))
        md5.update(password.encode('utf-8'))
        md5.update('SALT:)'.encode('utf-8'))
        return md5.hexdigest()

    def __verify_password(self):
        password = input('Verify your password: ')
        password = str(password)
        return self.__verify(self.__usrname, password), password

    def __verify(self, username, password):
        if self.__md5 != self.__calc_md5(username, password):
            return False
        return True

    def register(self):
        if self.__new is False:
            print('You have registered!')
            return
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        self.__usrname = str(username)
        self.__md5 = self.__calc_md5(str(username), str(password))
        print('Register complete!')
        self.__new = False

    def login(self):
        if self.__new is True:
            print('You haven\'t registered!')
            return
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        username = str(username)
        password = str(password)
        if username != self.__usrname:
            print('Failure! Wrong username or password!')
            return
        if self.__verify(username, password) is False:
            print('Failure! Wrong username or password!')
            return
        print('Login success!')
        self.__log_in = True

    def logoff(self):
        if self.__log_in is False:
            print('You didn\'t log in!')
            return
        self.__log_in = False
        print('Log off success!')

    def get_username(self):
        if self.__new is True:
            print('You haven\'t registered!')
            return
        if self.__log_in is False:
            print('Please log in first!')
            return
        print(self.__usrname)

    def set_username(self):
        if self.__new is True:
            print('You haven\'t registered!')
            return
        if self.__log_in is False:
            print('Please log in first!')
            return
        verify, password = self.__verify_password()
        if verify is False:
            print('Failure! Wrong password!')
            return
        username = input('Enter your new username: ')
        self.__usrname = str(username)
        self.__md5 = self.__calc_md5(self.__usrname, password)

    def set_password(self):
        if self.__new is True:
            print('You haven\'t registered!')
            return
        if self.__log_in is False:
            print('Please log in first!')
            return
        verify, password = self.__verify_password()
        if verify is False:
            print('Failure! Wrong password!')
            return
        password = input('Enter your new password: ')
        self.__md5 = self.__calc_md5(self.__usrname, password)

if __name__ == '__main__':

    u = User()
    u.login()
    u.set_username()
    u.register()
    u.login() # try with wrong username
    u.login() # try with wrong password
    u.login()
    u.get_username()
    u.set_username()
    u.set_password()
    u.logoff()
    u.get_username()
    u.set_username()
    u.set_password()
    u.register()
    u.login()
    u.logoff()
