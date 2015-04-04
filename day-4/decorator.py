#!/usr/bin/env python
# -*- coding=utf-8 -*-

def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

# now = log(now)
@log
def now():
	print '2015-03-04'

print now.__name__
# will print wrapper

if __name__ == '__main__':
	now()