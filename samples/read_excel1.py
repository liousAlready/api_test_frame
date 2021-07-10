# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 4:33 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : read_excel.py
# @Software: PyCharm

import os
import xlrd
from icecream import ic
from common.excel_utils import ExcelUtils

'''

测试封装代码

'''

excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '..', "samples/data/test_data.xlsx")
excel_Utils = ExcelUtils(excel_path, 'Sheet1')
# ic(excel_Utils.get_merged_cell_value(8, 0))
ic(excel_Utils.get_row_count())

sheet_list = []

## 获取表格数据
# for row in range(1, excel_Utils.get_row_count()):  #
#     row_dict = {}
#     row_dict['事件'] = excel_Utils.get_merged_cell_value(row, 0)
#     row_dict['步骤序号'] = excel_Utils.get_merged_cell_value(row, 1)
#     row_dict['步骤操作'] = excel_Utils.get_merged_cell_value(row, 2)
#     row_dict['完成情况'] = excel_Utils.get_merged_cell_value(row, 3)
#     sheet_list.append(row_dict)
#
# for row in sheet_list:
#     ic(row)

alldata_list = []

first_row = excel_Utils.sheet.row(0)  # 获取表格的第一行数据
# ic(first_row)

for row in range(1, excel_Utils.get_row_count()):  # 遍历循环出行
    row_dict = {}
    for col in range(0, excel_Utils.get_col_count()):  # 遍历循环出列
        row_dict[first_row[col].value] = excel_Utils.get_merged_cell_value(row, col)
    alldata_list.append(row_dict)

for row in alldata_list:
    ic(row)
