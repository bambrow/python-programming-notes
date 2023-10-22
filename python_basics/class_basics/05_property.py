#!/usr/bin/env python
# coding:utf-8


class Student():

    def __init__(self, name, score):
        self._name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if not isinstance(score, int):
            raise TypeError('Score must be an integer!')
        if not 0 <= score <= 100:
            raise ValueError('Score must between 0 - 100!')
        self._score = score

    @property
    def grade(self):
        if self._score < 60:
            return 'F'
        else:
            return 'P'


s1 = Student('Hailey', 75)
s2 = Student('Nina', 45)
print(s1.score)
print(s1.grade)
print(s2.score)
print(s2.grade)
s2.score = 95
print(s2.grade)
