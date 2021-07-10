# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 8:38 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : config_demo.py
# @Software: PyCharm


# 测试配置文件的demo

import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')

cfg = configparser.ConfigParser()
cfg.read(config_path)

print(cfg.get("default", "URL"))
print(cfg.get("path", "CASE_DATA_PATH"))
