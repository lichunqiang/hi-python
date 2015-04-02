#!/usr/bin/env python
# -*- coding=utf-8 -*-

def main(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	
	if x >= 0:
		return x
	else:
		return -x

def multi_return():

	return 1, 2

# 可变参数 number recived a tuple
def calcu(*numbers):
	print numbers

#关键字参数
def person(name, age, **kw):
	print 'name:', name, 'age:', age, 'other:', kw

def func(a, b, c = 0, *args, **kw):
	__doc__ = '''
	*args是可变参数，args接收的是一个tuple；
	**kw是关键字参数，kw接收的是一个dict'''

	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


if __name__ == '__main__':
	print main(1)

	a, b = multi_return()

	print a, b

	calcu(1, 2, 4)

	#把list或tuple的元素变成可变参数传进去
	calcu(*[1,2])

	person('light', 12)

	person('light', 12, grade = 'classify')

	kw = {'city': 'beijing', 'job': 'enginerr'}

	person('light', 12, **kw)

	func(1, 2)

	func(1, 2, c=3)

	func(1, 2, 3, 'a', 'b')

	func(1, 2, 3, 'a', 'b', x = 99)

	args = (1, 2, 3, 'a')

	kw = {'x': 99}

	func(*args, **kw)