#!/usr/bin/env python
# -*- coding=utf-8 -*-

from models import Student
from models import Book 

if __name__ == '__main__':
	book = Book()

	print book.get_name()

	book.set_name('python')

	print book.get_name()

 	print dir(Student)

 	print Student

	student = Student('light', 12)

	student.print_score()

	print student.get_db()
