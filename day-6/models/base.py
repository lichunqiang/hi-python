#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Base(object):
	"""docstring for Base"""
	__db = None

	def __init__(self, db):
		super(Base, self).__init__()
		self.__db = db


	def set_db(self, db):
		self.__db = db
	
	def get_db(self):
		return self.__db
