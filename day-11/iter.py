#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		super(Fib, self).__init__()
		self.a, self.b = 0, 1

	# return a iterable object
	def __iter__(self):
		return self
		
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration()

		return a

if __name__ == '__main__':
	for n in Fib():
		print n
