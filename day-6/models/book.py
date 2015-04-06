#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Book(object):
	"""docstring for Book"""
	__name = ''

	def __init__(self):
		super(Book, self).__init__()
		self.__name = __name__

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name
		
