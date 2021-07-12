# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 11:23 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : request_demo.py
# @Software: PyCharm


'''request 接口示例'''
import json

import requests

# 获取token
host = "https://api.weixin.qq.com"
params = {
    "grant_type": "client_credential",
    "appid": "wxb637f897f0bf1f0d",
    "secret": "501123d2d367b109a5cb9a9011d0f084",
}

res01 = requests.get(url=host + '/cgi-bin/token', params=params)

token = res01.json()['access_token']
print(token)
# 创建标签
host = "https://api.weixin.qq.com"
get_params = {
    "access_token": token
}
post_params = {"tag": {"name": "xzcqz112xzxq"}}
headers = {'content_type': 'application/json'}

res02 = requests.post(url=host + "/cgi-bin/tags/create", params=get_params, json=post_params, headers=headers)
print(res02.json())


