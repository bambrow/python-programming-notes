#!/usr/bin/env python
# coding:utf-8


class Animal():

    def __init__(self, name):
        self._name = name

    def eat(self):
        print("Animal " + str(self._name) + " is eating...")


class Dog(Animal):

    def eat(self):
        print("Dog " + str(self._name) + " is eating...")


animal = Animal("A")
dog = Dog("D")

animal.eat()
dog.eat()


def eat(animal):
    animal.eat()

eat(animal)
eat(dog)

