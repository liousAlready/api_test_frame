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

# str1 = 'come on! newdream'
# str2 = "china1usa2german3english"

pattern0 = re.compile(r"(\w+),(\w+) (\w+)(?P<sign>.*)")  # r 标识原生字符串
pattern1 = re.compile(r'come (\w+)!')
pattern2 = re.compile(r'\d+')

# result = re.match(pattern0, str1)  # 匹配以什么开头
# result = re.search(pattern1, str1)  # 扫描整个string查找匹配
# result = re.split(pattern2, str2)  # 扫描整个string查找匹配
# result = re.findall(pattern2, str2)  # 搜索string，以列表的形式返回全部能匹配的子串
# result = re.finditer(pattern2, str2)  # 返回的是迭代器
# for i in result:
#     print(i.group())

# print(result)


# print(result.string)
# print(result.re)
# print(result.pos)
# print(result.endpos)
# print(result.lastindex)
# print("~~~~~~~~~~~~~~~~~~~~~~")
# print(result.group())  # 匹配到的子串
# print(result.groups())
# print(result.groupdict())
# print(result.start())
# print(result.end())
# print(result.span())
# print(result.expand(r'\1'))


str1 = 'summer hot ~~'

pattern3 = re.compile(r'(\w+) (\w+)')


# str2 = (re.sub(pattern3, r'\2 \1', str2)) # 交换字符串位置
# str2 = (re.sub(pattern3, r'hello', str2))  # 替换字符串
# print(str2)

# result2 = re.match(pattern3, str2)
# print(result2.group(1).title())  # group(1).title()  首字母大写


def fun(m):
    return m.group(1).title() + ' ' + m.group(2).title()


str1 = re.sub(pattern3, fun, str1)
print(str1)

str2 = re.subn(pattern3, r'\2 \1', str1)
print(str2)

# 写法二：
str2 = "china1usa2german3english"
v_list = re.split(r'\d', str2)
print(v_list)
