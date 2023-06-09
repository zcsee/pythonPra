#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/9 09:57
@Author  : Jason
@Site    : 
@File    : demo7.py
@Project : leetcode
@Software: PyCharm
内容      : excel数据清理
"""

import pandas as pd

# import openpyxl

df = pd.read_excel('exam_demo.xlsx', skiprows=1)

# 筛选没有空分数的所有行
# print(df.loc[df['分数'].notnull(), :])

# 删除空列
df.dropna(axis='columns', inplace=True, how='all')


# 删除空行
# df.dropna(axis='rows', inplace=True, how='all')
df.dropna(axis='index', inplace=True, how='all')

# 将分数列为空的填充为0
df.fillna({'分数': 0}, inplace=True)
# df.loc[:, '分数'] = df['分数'].fillna(0)

# 填充名字，从上面的名字往下进行填充
# df.loc[:, '姓名'] = df['姓名'].fillna(method='ffill')
df['姓名'].fillna(method='ffill', inplace=True)

# 将清洗好的数据进行保存
# df.to_excel('exam_demo_clean.xlsx', index=False)


print(df)
