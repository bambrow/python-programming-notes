#!/usr/bin/env python
# coding:utf-8


class Animal():
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class RunnableMixIn():

    def run(self):
        print('running...')


class FlyableMixIn():

    def fly(self):
        print('flying...')


class Dog(Mammal, RunnableMixIn):
    pass


class Parrot(Bird, FlyableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Ostrich(Bird, RunnableMixIn):
    pass

