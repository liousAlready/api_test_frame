# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 6:40 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : testdata_utils.py
# @Software: PyCharm

import os
from common.excel_utils import ExcelUtils
from common import config  # 引用方法一读取配置文件
from common.localconfig_utlis import local_config  # 引用方法二读取配置文件

current_path = os.path.dirname(__file__)
# test_data_path = os.path.join(current_path, '..', config.CASE_DATA_PATH) # 方法一读取配置文件
test_data_path = os.path.join(current_path, '..', local_config.CASE_DATA_PATH)


class TestdataUtils():

    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(test_data_path, 'Sheet1').get_sheet_data_by_dict()  # excel的sheet1表的所有数据

    def __get_testcase_data_dict(self):
        '''将测试用例从excle取出来变成字典数据'''
        test_case_dict = {}
        for row_data in self.test_data:  # 行数据
            test_case_dict.setdefault(row_data['测试用例编号'], []).append(row_data)  # 转换成固定格式
        return test_case_dict

    def get_testcase_list(self):
        '''将测试用例从字典变成列表'''
        testcase_list = []
        for k, v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == "__main__":
    test = TestdataUtils()
    print(test.get_testcase_list())
    # for i in test.get_testcase_list():
    #     print(i)
