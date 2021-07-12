# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 10:08 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : log_demo.py
# @Software: PyCharm


'''测试日志的文件'''

import logging

logger = logging.getLogger('logger')
logger.setLevel(10)  # 10,20,30,40,50   设置出事日志的级别
# logger.setLevel(logging.DEBUG)  # 定义日志的级别  # 全局

handler1 = logging.StreamHandler()  # 输出到控制台
handler1.setLevel(30)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")  # 这里需要注意保持格式的统一
handler1.setFormatter(formatter)
logger.addHandler(handler1)


handler2 = logging.FileHandler('./test.log', 'a', encoding="utf-8")  # a表示追加文件
handler2.setLevel(10)
handler2.setFormatter(formatter)
logger.addHandler(handler2)


logger.info("hello")
