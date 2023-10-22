#!/usr/bin/env python
# coding:utf-8


class Student(): # Python 2: class_basics Person(Object):
    """
    Define a student.
    """
    def __init__(self, name, age, sex, id_num):
        self.__name = name # private variable
        self.__age = age
        self.__sex = sex
        self.__id = id_num

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_sex(self):
        return self.__sex

    def get_id_num(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def to_string(self):
        return "name: " + str(self.__name) + " age: " + str(self.__age) + " sex: " + str(self.__sex) + " id: " + str(self.__id)

if __name__ == '__main__':

    student = Student('Hailey', 21, 'Female', 110565)
    print(student.to_string())
