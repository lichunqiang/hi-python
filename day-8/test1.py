#!/usr/bin/env python
# -*- coding=utf-8 -*-

from models import *

def run_twice(animal):
	animal.run()
	animal.run()

if __name__ == '__main__':
	run_twice(Cat())
	run_twice(Dog())
