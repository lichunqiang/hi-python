#!/usr/bin/env python
# -*- coding=utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name

	@property
	def name(self):
	    return self._name

	@name.setter	
	def name(slef, name):
		slef._name = name

	def __str__(self):
		return 'Student Object (name: %s)' % self.name
		

if __name__ == '__main__':
	print Student('light')
