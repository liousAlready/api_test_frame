# -*- coding: utf-8 -*-
# @Time    : 2021/7/15 4:18 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : re_demo.py
# @Software: PyCharm


import re

'''

正则取值

re模块使用

'''

# newdream

str1 = 'newdream,come on!'
pattern = re.compile(r"(\w+),(\w+) (\w+)(?P<sign>.*)")  # r 标识原生字符串

result = re.match(pattern, str1)  # 匹配以什么开头
# print(result)
print(result.string)
print(result.re)
print(result.pos)
print(result.endpos)
print(result.lastindex)
print("~~~~~~~~~~~~~~~~~~~~~~")
print(result.group())  # 匹配到的子串
print(result.groups())
print(result.groupdict())
print(result.start())
print(result.end())
print(result.span())
print(result.expand(r'\2+\3+\1+\4'))
