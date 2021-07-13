# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 4:51 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : requests_demo01.py
# @Software: PyCharm

import requests

response = requests.get('http://www.hnxmxit.com/')
# print(response.json())
# response.encoding = 'utf-8'
# print(response.text)

# print(response.content.decode('utf-8'))
# print(response.apparent_encoding)
# print(response.headers)