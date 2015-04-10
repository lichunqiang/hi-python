#!/usr/bin/env python
# -*- coding=utf-8 -*-

from types import MethodType

class Student(object):
	"""docstring for Student"""
	pass


def set_age(self, age):
	self.age = age

if __name__ == '__main__':
	s = Student()
	s.name = 'light' # bind a attribute for the instance
	print s.name


	s.set_age = MethodType(set_age, s, Student)

	s.set_age(25) # invoke intance method

	print s.age

	s2 = Student()

	try:
		s2.set_age(2)
	except Exception, e:
		def set_score(self, score):
			self.score = score
        #bind method for the class
		Student.set_score = MethodType(set_score, None, Student)


		s2.set_score(2)
		print s2.score

		s.set_score(10)
		print s.score


		
