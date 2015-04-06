#!/usr/bin/env python
# -*- coding=utf-8 -*-

from .base import Base

class Student(Base):
	"""docstring for Student"""
	def __init__(self, name, age):
		super(Student, self).__init__('db_name')
		self.name = name
		self.age = age

	def print_score(self):
		print '%s: %s' % (self.name, self.age)

		
	def __str__(self):
		return 'My name %s' % __name__
