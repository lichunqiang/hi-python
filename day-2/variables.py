#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. 在内存中创建一个'ABC'的字符串
# 2. 在内容中创建一个名为a的变量，并把它指向'ABC'
a = 'ABC'

print 'The variable a is', a

# -----------------------------------

a = 'ABC'

# a 和 b 同时指向 'ABC' 内存地址
b = a 

# a 指向 'XYZ' 的内存地址，但 b 仍然指向 'ABC'
a = 'XYZ'

print 'the variable b is', b

# b is ABC

#---------------unicode-----------------------------
print u'测试中文'

#------------------List------------------------

classmates = ['light', 'Machile', 'Bob']

print classmates
# 打印List的长度
print len(classmates)

print classmates[0]

print classmates[1]
# the last one
print classmates[-1]
# 追加到末尾
classmates.append('Adam')
print classmates

# 插入到指定位置
classmates.insert(1, 'Jack')

print classmates

#删除并返回List最后一个元素
last = classmates.pop()
print classmates, last

#----------tuple-----------tuple的每个元素，指向永远不变--------

classmates = ('light', 'jack')

classmates = ('a', 'b', ['A', 'B'])

classmates[2][0] = 'X'

for i in classmates:
	print i

if True:
	pass

# ---------------------dict---------

d = {'light': 100, 'jack': 60}

print d['light']

d['Adam'] = 80

print d

# 判断某个key是否存在dict中
print 'test' in d
# 或者使用get，如果key不存在放回None，同时也可以指定value
print d.get('test')
print d.get('test', -1)

#删除
data = d.pop('light')
print data
print d

#--------------set--------
#在set中，没有重复的key,重复元素在set中自动被过滤
a = set([1, 2, 3])
print a
a.add(4)
print a
a.remove(3)
print b, a

# 计算两个set的交集和并集
b = set([1, 4, 5])

print a & b

print a | b

def main():
	print __name__



if __name__ == '__main__':
	main()