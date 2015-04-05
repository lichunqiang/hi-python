#!/usr/bin/env python
# -*- coding=utf-8 -*-

import web
import web.utils  as u


print web.__author__
print web.__email__
print web.__doc__


print u.__doc__
print u.now.__doc__
u.now()


if __name__ == '__main__':
	u.show_path()
