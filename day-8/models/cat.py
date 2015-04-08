#!/usr/bin/env python
# -*- coding=utf-8 -*-

from .animal import Animal

class Cat(Animal):
	"""docstring for Cat"""
	def __init__(self):
		super(Cat, self).__init__()
		self.name = 'Cat'

	def run(self):
		print '%s is running...' % self.name		
		
