# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 4:33 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : read_excel.py
# @Software: PyCharm

import os
import xlrd
from icecream import ic

# os.path.dirname(__file__)  读取当前文件的路径
# os.path.join(os.path.dirname(__file__),'data/test_data.xlsx') 拼接路径
excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
ic(excel_path)

wb = xlrd.open_workbook(excel_path)

wb = xlrd.open_workbook(excel_path)  # 创建工作蒲对象
sheet = wb.sheet_by_name('Sheet1')  # 创建表格对象
# cell_value = sheet.cell_value(3, 2)  # 读取对象，行列下标从0开始
cell_value = sheet.cell_value(0, 0)  # 读取对象，行列下标从0开始
ic(cell_value)
cell_value = sheet.cell_value(1, 0)  # 读取对象，行列下标从0开始
ic(cell_value)
cell_value = sheet.cell_value(2, 0)  # 对于合并的左上角首个单元格会返回真实值
ic(cell_value)

merged = sheet.merged_cells  # 读取对象，行列下标从0开始
# 处理方式： xlrd
ic(sheet.merged_cells)  # 返回一个列表 起始行，结束行，起始列，结束列  获取表格里面合并的所有单元格
# 逻辑：凡是在合并 merged_cells 属性范围内的单元格，它的值都要等于左上角的值
row_index = 3
col_index = 0

cell_value = 0
for (rlow, rhigh, clow, chigh) in merged:  # 便利表格中的所有元素
    if (row_index >= rlow and row_index < rhigh):  # 行坐标的判断 1<=3<5
        if (col_index >= clow and col_index < chigh):  # 列坐标 0<=0<1
            # 如果满足条件，就把合并单元格第一个位置的值赋给其他合并单元格
            cell_value = sheet.cell_value(rlow, clow)
ic(cell_value)


def get_merged_cell_value(row_index, col_index):
    cell_value = 0
    for (rlow, rhigh, clow, chigh) in merged:  # 便利表格中的所有元素
        if (row_index >= rlow and row_index < rhigh):  # 行坐标的判断 1<=3<5
            if (col_index >= clow and col_index < chigh):  # 列坐标 0<=0<1
                # 如果满足条件，就把合并单元格第一个位置的值赋给其他合并单元格
                cell_value = sheet.cell_value(rlow, clow)
    return cell_value


ic(get_merged_cell_value(4, 0))
