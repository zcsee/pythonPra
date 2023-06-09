#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/8 14:23
@Author  : Jason
@Site    : 
@File    : demo6.py
@Project : leetcode
@Software: PyCharm
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data21.csv')
df.plot()
plt.show()

# print(df.corr())

