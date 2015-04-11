#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name

	def __call__(self):
		print 'My name is %s.' % self.name


if __name__ == '__main__':
	s = Student('light')

	print callable(s)
	s()
		
