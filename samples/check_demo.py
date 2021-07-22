# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 4:44 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : check_demo.py
# @Software: PyCharm


import re
import ast

# 正则匹配测试


# class Check():
#
#     def __init__(self, response):
#         self.response = response


# 实际结果：
import re

str1 = '{"access_token": "47_aDXRi0v1PuAa_bPoRBUZ0sorObe33xE-TaSQmbGEopx5eiVa-u79f3EgK-2NqWtPGQ18ENPHY1PDWCkddKkMzRh6k4mHkGyAcxvDeblsWkNQMNz6OVXBzjMawNrb733vsGlnm4YeNQSHMGTcQFAhACAHWR","expires_in": 7200}'
# 期望解决：
str2 = '{"access_token": "(.+?)","expires_in": (.+?)}'

# if re.findall(str2, str1):
#     print(True)
# else:
#     print(False)

# 是否包含 json key
jsondata1 = ast.literal_eval(str1)
str2 = "access_token,expires_in"
check_key_list = str2.split(',')
for check_key in check_key_list:
    result = True
    if check_key in jsondata1.keys():
        result = True
    else:
        result = False
    if not result:
        break
# print(check_key_list)
print(result)

# print('access_token' in jsondata1.keys())

# 键值对正确的情况
str2 = '{"expires_in: 7200"}'
print(ast.literal_eval(str2) in jsondata1.items())
