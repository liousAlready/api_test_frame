# -*- coding: utf-8 -*-
# @Time : 2021/7/21 17:11
# @Author : Limusen
# @File : check_demo


import re
import ast

# 　正则匹配测试

# 　实际结果
str1 = '{"access_token":"47_WPQUn0NY74nAn0MDowRGXaRCyBmEuyTmpdYGn44sJwqH9XXjSdog1ksQKWTQ3UsiPLMXDIyRsbFRJ5tcxq_cLQIjKkZPrCL1_JgwYJUxYcCecHRMFKNhVIoGsfGrci2nMSutz9vtWvYDaekzGYEiABALDJ","expires_in": 7200}'

# 期望结果

str2 = '{"access_token":"(.+?)","expires_in":(.+?)}'

if re.findall(str2, str1):
    print(True)
else:
    print(False)

# 　是否包含json key

jsondata1 = ast.literal_eval(str1)
str2 = 'access_token,expires_in'
check_key_list = str2.split(',')
for che_key in check_key_list:
    result = True
    if che_key in jsondata1.keys():
        result = True
    else:
        result = False
    if not result:
        break
print(result)
# print(jsondata1.keys())
# 　键值对正确的情况


str2 = '{"expires_in": 7200}'
print(jsondata1.items())
