# -*- coding: utf-8 -*-
#print abs value of an integer
a = input('INPUT:')
if a >= 0:
	print a
else:
	print 'ABS:',-a


#使用raw_input()只能输入字符串
#使用input会自动将输入的值转换成对应的类型，如需输入字符或字符串必须用引号，否则报错