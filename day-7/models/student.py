#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @see http://python-china.org/topic/725

__all__ = ['Student']

class Student(object):
	"""docstring for Student"""
	def __init__(self):
		super(Student, self).__init__()
	
	def set_name(self, name):
		self.name = name	
			
	def get_name(self):
		return self.name


class StudentClass(object):
	"""docstring for StudentClass"""
	def __init__(self, arg):
		super(StudentClass, self).__init__()
		self.arg = arg
		
