#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/8 10:20
@Author  : Jason
@Site    : 
@File    : demo3.py
@Project : leetcode
@Software: PyCharm
内容      : pandas查看数据
"""

import pandas as pd

df = pd.read_csv('data.csv')

# 打印前10行数据
# print(df.head(10))

# 打印最后10行数据
# print(df.tail(10))

# 查看数据的信息
print(df.info())
