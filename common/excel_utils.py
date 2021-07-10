# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 10:03 上午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : excel_utils.py
# @Software: PyCharm


import os
import xlrd  # 内置模块放第一  第三方pip install  第三放自定义模块
from icecream import ic


class ExcelUtils():

    def __init__(self, filepath, sheet_name):
        self.filepath = filepath
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  # 定义一个类属性

    def get_sheet(self):
        '''获取表格对象'''
        wb = xlrd.open_workbook(self.filepath)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def get_row_count(self):
        '''获取行'''
        row_count = self.sheet.nrows
        return row_count

    def get_col_count(self):
        '''获取列'''
        col_count = self.sheet.ncols
        return col_count

    def get_cell_value(self, row_index, col_index):
        '''赋值给指定单元格'''
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_info(self):
        '''获取所有合并单元信息'''
        merged_info = self.sheet.merged_cells
        return merged_info

    def get_merged_cell_value(self, row_index, col_index):
        '''既能获取普通单元格数据又能获取合并单元格数据'''
        cell_value = 0
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():  # 便利表格中的所有元素
            if (row_index >= rlow and row_index < rhigh):  # 行坐标的判断 1<=3<5
                if (col_index >= clow and col_index < chigh):  # 列坐标 0<=0<1
                    # 如果满足条件，就把合并单元格第一个位置的值赋给其他合并单元格
                    cell_value = self.get_cell_value(rlow, clow)
                    break  # 防止循环判断 出现值覆盖的情况
                else:
                    cell_value = self.get_cell_value(row_index, col_index)
            else:
                cell_value = self.get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_data_by_dict(self):
        '''获取整个excel表格数据，通过字典的方式返回'''
        alldata_list = []
        first_row = self.sheet.row(0)  # 获取表格的第一行数据
        for row in range(1, self.get_row_count()):  # 遍历循环出行
            row_dict = {}
            for col in range(0, self.get_col_count()):  # 遍历循环出列
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            alldata_list.append(row_dict)
        return alldata_list


if __name__ == "__main__":
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '..', "samples/data/test_data.xlsx")
    excel_Utils = ExcelUtils(excel_path, 'Sheet1')
    ic(excel_Utils.get_merged_cell_value(8, 0))
    ic(excel_Utils.get_merged_cell_value(3, 0))
    #
    # 测试代码模块边界值
    for i in range(1, 9):
        ic(excel_Utils.get_merged_cell_value(i, 0))

    ic(excel_Utils.get_sheet_data_by_dict())
