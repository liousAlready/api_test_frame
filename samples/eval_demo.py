# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 4:32 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : eval_demo.py
# @Software: PyCharm
import ast

sum = eval("66+72")
print(sum)

print(eval("{'name':'lms'}"))

print(eval("{'name':'lms','age':118}", {'age': 18}))

# 传入局部变量的值
print("传入局部变量的值,转换到变量:", eval("{'name':'lms','age':age}", {'age': 18}))

age = 10
print(eval("{'name':'lms','age':age}", {'age': 18}, locals()))  # 全局变量

# 删除文件
# eval("__import__('os').system('rm -rf ./a.txt')" )

# eval("__import__('os').system('ls')" )

# print(ast.literal_eval("{'name':'asd','age':118}"))
