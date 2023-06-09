#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/7 14:46
@Author  : Jason
@Site    : 
@File    : demo1.py
@Project : leetcode
@Software: PyCharm
"""
import pandas as pd

#
# my_data_set = {
#     'cars': ['BMW', "BYD", "Ford"],
#     'passing': [3, 7, 2]
# }
#
# my_var = pd.DataFrame(my_data_set)
#
# print(my_var)
# print(pd.__version__)


# a = [1, 7, 2]
#
# my_var = pd.Series(a, index=['a', 'b', 'c'])
#
# print(my_var)
#
# print(my_var['b'])
#
# calories = {'day1': 111, 'day2': 222, 'day3': 333}
# my_calories = pd.Series(calories, index=['day1', 'day2'])
#
# print(my_calories)
# print(my_calories['day2'])


# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

# 使用index指定行名称
# my_var = pd.DataFrame(data, index=['day1', 'day2', 'day3'])

# print(my_var)
# 打印第一行的内容
# print(my_var.loc[0])
# 查看打印一行时，返回的数据类型
# print(f'dataframe获取一行时的类型:{type(my_var.loc[0])}')

# 打印第一、二行
# print(my_var.loc[[0, 1]])
# print(f"dataframe获取多于一行后的类型:{type(my_var.loc[[0, 1]])}")

# 根据行的index打印行
# print(f"行的index为day2的数据\n{my_var.loc['day2']}")


# 读取csv文件
df = pd.read_csv('data.csv')

# 打印csv的文件内容
print(df)

"""
In my system the number is 60, which means that if the DataFrame contains more than 60 rows, 
the print(df) statement will return only the headers and the first and last 5 rows.
"""
# 查看默认的返回行数,超过60则只返回前后的5行
print(pd.options.display.max_rows)

# 修改max_rows为9999
pd.options.display.max_rows = 9999
print(df)
