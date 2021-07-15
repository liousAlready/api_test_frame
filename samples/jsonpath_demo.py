# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 6:49 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : jsonpath_demo.py
# @Software: PyCharm
import jsonpath

d1 = {
    "access_token": "47_S6vqKdF_eLtvd86KPrBkTjJsUZx4zI4w01kFbT1eJbJOx0-N0-TBalN-u31ECPw4U1aI1YPWJhNYrjyBe2EvSf80WCbX8HR7wjqO4-Od-rN5oISqhrur5zbEGd8vajzPfZbadDQ0anYKXE5jITPfAEAEPL"}

print(d1['access_token'])

d2 = {
    "tags": [{
        "id": 1,
        "name": "每天一罐可乐星人",
        "count": 0
    },
        {
            "id": 2,
            "name": "星标组",
            "count": 0
        },
        {
            "id": 127,
            "name": "广东",
            "count": 5
        }
    ]}

print(d2['tags'][1]["name"])
print(jsonpath.jsonpath(d1, '$.access_token')[0])
print(jsonpath.jsonpath(d2, '$.tags[1].name')[0])
