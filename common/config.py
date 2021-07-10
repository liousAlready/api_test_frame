# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 8:45 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : config.py
# @Software: PyCharm

'''取配置文件方式一 --002'''

import os
from common.config_utils import ConfigUtils

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')
configUtils = ConfigUtils(config_path)

URL = configUtils.read_value('default', "URL")
CASE_DATA_PATH = configUtils.read_value('path', "CASE_DATA_PATH")
