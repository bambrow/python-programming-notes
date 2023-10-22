#!/usr/bin/env python
# coding:utf-8


def fn(self, name='world'):
    print('Hello {0}'.format(name))

Hello = type('Hello', (object,), dict(hello=fn))
# create Hello class
# parameters: class name, superclasses in a tuple, names of methods of class (and tied to functions)
h = Hello()
h.hello()


# metaclass is the template of classes, so we put 'type' in the parentheses
class ListMetaclass(type):
    # parameters: the object of the class ready to create, class name, superclasses, methods
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# use ListMetaclass.__new__() to create this class
class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
print(l)
