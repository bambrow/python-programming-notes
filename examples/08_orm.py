#!/usr/bin/env python
# coding:utf-8


class Field:

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<{0}:{1}>'.format(self.__class__.__name__, self.name)


class StringField(Field):

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        # to avoid changing Model class
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: {0}'.format(name))
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: {0} -> {1}'.format(k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '{0}'".format(key))

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into {0} ({1}) values ({2})'.format(self.__table__, ','.join(fields), ','.join(params))
        print('SQL: {0}'.format(sql))
        print('ARGS: {0}'.format(str(args)))


class User(Model):

    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=111, name='Jack', email='jack@orm.com', password='jackpswd')
u.save()
