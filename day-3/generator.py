#!/usr/bin/env python
# -*- coding=utf-8 -*-

l = [x * x for x in range(10)]
g = (x * x for x in range(10))

print l, g

for n in g:
	print n


# 1 1 2 3 5...
def fib(max):
	n, a, b = (0, 0, 1)
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

if __name__ == '__main__':
	print fib(5)

	for i in fib(5):
		print i