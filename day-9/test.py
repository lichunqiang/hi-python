#!/usr/bin/env python
# -*- coding=utf-8 -*-

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		super(MyObject, self).__init__()
		self.x = 9
	def power(self):
		return self.x * self.x


if __name__ == '__main__':
	obj = MyObject()

	print hasattr(obj, 'x')
	print obj.x

	print hasattr(obj, 'y')


	setattr(obj, 'y', 19)

	print hasattr(obj, 'y')

	print getattr(obj, 'y')

	print obj.y		
