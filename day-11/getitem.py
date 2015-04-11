#!/usr/bin/env python
# -*- coding=utf-8 -*-


class  Fib(object):
	"""docstring for  Fib"""
	def __init__(self):
		super( Fib, self).__init__()
		
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

# support slice
class Fib2(object):
	"""docstring for Fib2"""
	def __init__(self):
		super(Fib2, self).__init__()
		
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop	
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x > start:
					L.append(a)
				a, b = b, a + b
			return L

if __name__ == '__main__':
	f = Fib()

	print f[0]

	f1 = Fib2()
	print f1[0: 5]
