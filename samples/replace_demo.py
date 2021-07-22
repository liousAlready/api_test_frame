# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 11:56 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : replace_demo.py
# @Software: PyCharm
import ast
import re

import requests

tmep_variables = {"token": "123123"}

params = '{"access_token":${token}}'  # 建议考虑1个以上的情况
value = re.findall('\\${\w+}', params)[0]
print(value)
params = params.replace(value, tmep_variables.get(value[2:-1]))
print(params)

# 替换多个值
tmep_variables = {"token": "123123", "number": "1231412424", "age": "90"}
str1 = "{'access_token':${token}, ${age}==>${number}}"
# for v in re.findall('\\${\w+}', str1):
#     str1 = str1.replace(v, tmep_variables.get(v[2:-1]))
# print(str1)


str1 = re.sub('\\${\w+}', r'123456', str1, 1)
print(str1)

# print(eval("{'name':'lix','age':${age}},{'${age}':18"))

# dicta = {"token": "123", "age": 18}
# print(dicta["token"])
# print(dicta.get("token"))

# print(value)

# url = "/cgi-bin/token"
#
# requests.get(url,
#              params=ast.literal_eval(params)
#              )

temp_variables = {}
temp_variables = {"token": "7_0oWGEQdTsa6p2nbKw2"}
