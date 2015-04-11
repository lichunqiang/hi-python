#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Student(object):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
		
	def __getattr__(self, attr):
		if attr == 'age':
			return 23
		raise AttributeError('Student object has no attribute %s' % attr)


class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path = ''):
		super(Chain, self).__init__()
		self._path = path
		
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

if __name__ == '__main__':
	s = Student()

	print s.name 
	print s.age

	print Chain().status.user.limit
