#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""Simple ORM using metaclass
理解元类：
http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386820064557c69858840b4c48d2b8411bc2ea9099ba000
"""

__author__ = 'Light'

class Field(object):
	"""docstring for Field"""
	def __init__(self, name, column_type):
		super(Field, self).__init__()
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
	"""docstring for StringField"""
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	"""docstring for IntegerField"""
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaClass(type):
	"""docstring for ModelMetaClass"""
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print 'Found model: %s' % name
		mappings = dict()

		for k, v in attrs.iteritems():
			if isinstance(v, Field):
				print 'found mapping: %s ===> %s' % (k, v)
				mappings[k] = v
		for v in mappings.iterkeys():
			attrs.pop(k)

		attrs['__mappings__'] = mappings
		attrs['__table__'] = name

		return type.__new__(cls, name, bases, attrs)

class Model(dict):
	"""docstring for Model"""

	__metaclass__ = ModelMetaClass	

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
						
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.iteritems():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))

		sql = 'insert into  %s (%s) values (%s)' % (self.__table__, ','.join(fields, ','.join(params)))

		print 'SQL: %s' . sql
		print 'ARGS: %s' % str(args)

		
class User(Model):
	"""docstring for User"""
	
	id = IntegerField('uid')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')



if __name__ == '__main__':
	u = User(id = 1, name = 'light', email = 'light-li@Hotmail.com', password = '123')
	u.save()		
