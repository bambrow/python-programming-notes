#!/usr/bin/env python
# coding:utf-8

import json

d = dict(name='Hailey', age=21, score=95)
print(json.dumps(d))
s = json.dumps(d)
d2 = json.loads(s)
print(d2)


class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

student = Student('Hailey', 21, 95)
print(json.dumps(student, default=student2dict))
s = json.dumps(student, default=student2dict)
student2 = json.loads(s, object_hook=dict2student)
print(student2)
