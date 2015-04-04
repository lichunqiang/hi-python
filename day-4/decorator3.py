#!/usr/bin/env python
# -*- coding=utf-8 -*-

def log(*args):
	def decorator(func):
		def wrapper(*args, **kw):
			print 'befor call %s()' % func.__name__
			result = func(*args, **kw)
			print 'after call %s()' % func.__name__
			return result
		return wrapper
	return decorator


@log('test')
def now():
	print '2015'


if __name__ == '__main__':
	now()
