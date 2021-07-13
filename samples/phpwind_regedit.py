# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 7:31 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : phpwind_regedit.py
# @Software: PyCharm


'''php论坛注册demo'''
import requests
import re


'''

需要用到session关联

'''


session = requests.Session()
'''打开注册页面'''
hosts = "http://47.107.178.45"
login_params = {
    'm': 'u',
    'c': "register"
}

res01 = session.get(url=hosts + "/phpwind/index.php", params=login_params)
csrf_token = re.findall('csrf_token" value="(.+?)"', res01.content.decode("utf-8"))[0]
print(res01.url)
print(csrf_token)

'''注册'''
url_encode_data = {
    "username": "lizxmama",
    "password": "123456",
    "repassword": "123456",
    "email": "zxnnaq12z31@qq.com",
    "csrf_token": csrf_token
}
param_info = {
    'm': 'u',
    'c': "register",
    'a': "dorun"
}

res02 = session.post(url=hosts + "/phpwind/index.php",
                     params=param_info,
                     data=url_encode_data
                     )
print(res02.url)
print(res02.content.decode("utf-8"))
