#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/8 10:13
@Author  : Jason
@Site    : 
@File    : demo2.py
@Project : leetcode
@Software: PyCharm
"""

import pandas as pd

# # 读取json文件
# df = pd.read_json('data.json')
#
# # 打印json内容，超过60行， 中间被省略
# print(df)
#
# # 打印json文件全部内容，使用to_string函数
# print(df.to_string())

"""
将python的dict类型直接导入到dataframe
"""

# dict类型的数据
data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

# 将dict类型的变量格式化为dataframe
df = pd.DataFrame(data)

print(df)
