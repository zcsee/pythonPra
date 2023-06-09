#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/8 10:32
@Author  : Jason
@Site    : 
@File    : demo4.py
@Project : leetcode
@Software: PyCharm
内容      : 清理数据
"""

import pandas as pd

df = pd.read_csv('datawrong.csv')

"""
删除包含空值的行
"""

# 将存在空值的行去除，重新生成一个dataframe
# new_df = df.dropna()

# 将存在空值的行去除，在原文件修改
# df.dropna(inplace=True)

# print(new_df.to_string())
# print(df.to_string())

"""
将空值用指定值替代
"""

# 对所有列进行替换，有时候不符合预期
# new_df = df.fillna(130)
# print(new_df.to_string())

# 对指定列进行替换
# df['Calories'].fillna(130, inplace=True)
# df['Date'].fillna("'2020/12/22'", inplace=True)
# print(df.to_string())

# 用平均值，中位数，众数来进行替换

# # 获取平均值
# x = df['Calories'].mean()
# # 使用平均值进行空值填充
# df['Calories'].fillna(x, inplace=True)

# 获取中位数
# y = df['Calories'].median()
# df['Calories'].fillna(y, inplace=True)

# 获取众数
# z = df['Calories'].mode()[0]
# df['Calories'].fillna(z, inplace=True)
# 
# # print(z)
# 
# print(df.to_string())

"""
清理错误格式的数据
"""

# 修改前数据
# print(df.to_string())

# 将指定列存在空值的行去除
# df.dropna(subset=['Date'], inplace=True)

# 将Date列的数据类型统一修改成datatime
# df['Date'] = pd.to_datetime(df['Date'])
# print(df.to_string())


"""
Set "Duration" = 45 in row 7:
"""

# 将第7行Duration列的值设置成45
# df.loc[7, 'Duration'] = 45
# print(df.to_string())


"""
针对值进行数据清洗
"""

# df.index -- 行号
# print(df.index)

# 逐行查看Duration字段，如果大于120，则设置成120
# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.loc[x, 'Duration'] = 120

# 逐行查看Duration字段，如果大于120，则整行删除
# for x in df.index:
#     if df.loc[x, 'Duration'] > 120:
#         df.drop(x, inplace=True)
#
# print(df.head(20).to_string())

"""
发现重复的行
"""
# print(df.duplicated())

# 删除重复的行
print(df.drop_duplicates(inplace=True))
print(df.head(15).to_string())

