#!/usr/bin/env python
# -*- coding=utf-8 -*-


class Student(object):
	"""docstring for Student"""

	@property
	def birth(self):
	    return self._birth

	@birth.setter
	def birth(self, value):
		if not isinstance(value, int):
			raise ValueError('must be int')
		self._birth = value

	@property
	def age(self):
	    return 2014 - self._birth


if __name__ == '__main__':
	# Stundet's age is readonly
	# birth is can read and write

	s = Student()


	s.birth = 12

	print s.age


	s.age = 12
