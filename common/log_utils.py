# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 10:27 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : log_utils.py
# @Software: PyCharm

import logging
import os
import time

from common.localconfig_utlis import local_config

current_path = os.path.dirname(__file__)
log_output_path = os.path.join(current_path, '..', local_config.LOG_PATH)


class LogUtil():

    def __init__(self, log_path=log_output_path):
        self.log_name = os.path.join(log_output_path, 'ApiTest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger("ApiTest")  # 设置日志文件名为 ApiTest
        self.logger.setLevel(local_config.LOG_LEVEL)
        # 控制台输出配置
        console_hander = logging.StreamHandler()  # 输出到控制台
        file_hander = logging.FileHandler(self.log_name, 'a', encoding="utf-8")  # 输出到文件
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")  # 这里需要注意保持格式的统一
        console_hander.setFormatter(formatter)
        file_hander.setFormatter(formatter)

        self.logger.addHandler(console_hander)  # 写入
        self.logger.addHandler(file_hander)  # 写入
        console_hander.close()  # 防止日志打印重复
        file_hander.close()  # 关闭连接

    def get_log(self):
        return self.logger


logger = LogUtil().get_log()  # 防止日志打印重复

if __name__ == "__main__":
    logger.info("测试代码")
