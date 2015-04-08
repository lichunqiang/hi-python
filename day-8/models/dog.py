#!/usr/bin/env python
# -*- coding=utf-8 -*-

from .animal import Animal

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()
		self.name = "Dog"

	def run(self):
		print '%s is running...' % self.name
		

