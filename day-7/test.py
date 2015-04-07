#!/usr/bin/env python
# -*- coding=utf-8 -*-

from models import Student
try:
	from models import student
except Exception, e:
	raise e

if __name__ == '__main__':
	print student.__all__
	student  = Student()

	student.set_name('light')

	print student.get_name()
