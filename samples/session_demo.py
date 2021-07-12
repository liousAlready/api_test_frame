# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 2:20 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : session_demo.py
# @Software: PyCharm


# 用request完成论坛发帖

import requests
import re
from collections import OrderedDict

host = 'http://47.107.178.45'

session = requests.Session()  # 创建session对象

# 01.进入论坛首页
res01 = session.get(url=host + '/phpwind/')
body01 = res01.content.decode("utf-8")
token_id = re.findall('name="csrf_token" value="(.+?)"/>', body01)[0]  # 正则表达式 findall  前段是截取的内容，后面是正文

# 02.登录获取token
get_params = {
    "m": "u",
    "c": "login",
    "a": "dologin"
}
post_params = {
    "username": "limusen",
    "password": "limusen",
    "csrf_token": token_id,
    "csrf_token": token_id
}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
res02 = session.post(url=host + '/phpwind/index.php',
                     params=get_params, data=post_params,
                     headers=headers
                     )
body02 = res02.content.decode('utf-8')
# print(body02)

login_id = re.findall('_statu=(.+?)",', body02)[0]
# print(login_id)

# 03.授权页面
get_params = {
    "m": "u",
    "c": "login",
    "a": "welcome",
    "_statu": login_id

}
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
res03 = session.get(url=host + '/phpwind/index.php',
                    params=get_params, headers=headers
                    )
# print(res03.content.decode("utf-8"))

# 04.发帖
get_params = {
    "c": "post",
    "a": "doadd",
    "_json": 1,
    "fid": 73
}

headers_info = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary8p1efq7ICaooKJCX",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

mul_form_data = OrderedDict(
    [
        ("atc_title", (None, "request测试001")),
        ("atc_content", (None, "就这就这？？？")),
        ("pid", (None, "")),
        ("tid", (None, "")),
        ("special", (None, "default")),
        ("reply_notice", (None, 1)),
        ("csrf_token", (None, token_id))
    ]
)

res04 = session.post(url=host + '/phpwind/index.php',params=get_params,headers=headers,files=mul_form_data)
print(res04.content.decode("utf8"))
