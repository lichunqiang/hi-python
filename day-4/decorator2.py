#!/usr/bin/env python
# -*- coding=utf-8 -*-
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s, call %s()' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator

# now = log('excude')(now)
@log('excude')
def now():
	print '2015-03-04'


print now.__name__

if __name__ == '__main__':
	now()