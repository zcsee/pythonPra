#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/8 11:16
@Author  : Jason
@Site    : 
@File    : demo5.py
@Project : leetcode
@Software: PyCharm
内容      : 查看server数据
"""
import re

import pandas as pd

df = pd.read_csv('server_vb.csv')

# print(df.head(10).to_string())

# print(df[['svr_id',
#           'svr_asset_id',
#           'svr_device_name',
#           'svr_sn',
#           'svr_device_type',
#           'svr_rack_name',
#           'svr_pos_id',
#           'svr_lan_ip',
#           'svr_raid_type',
#           'svr_os_name',
#           'svr_producer']].head(10).to_string())
# df['svr_device_name'].dropna(inplace=True)

# 将svc_device_name为空字段的填充为DELl
df['svr_device_name'].fillna('DELL', inplace=True)

# print(df['svr_device_name'].to_string())

# cond = df['svr_device_name'].str.contains("基础支撑")

# print(df[cond].to_string())
# print(cond.to_string())

# print(df[cond][['svr_id',
#                 'svr_asset_id',
#                 'svr_device_name',
#                 'svr_sn',
#                 'svr_device_type',
#                 'svr_rack_name',
#                 'svr_pos_id',
#                 'svr_lan_ip',
#                 'svr_raid_type',
#                 'svr_os_name',
#                 'svr_producer']].to_string())

"""
正则匹配
"""


# 通过正则匹配将指定字段包含关键字的行找出来
def func(x):
    if re.search(".*TCS.*", x) or re.search(".*基础支撑.*", x):
        return True
    else:
        return False


# 筛选过的行，打印指定的列
# print(df[df['svr_device_name'].apply(func)][['svr_asset_id',
#                                              'svr_device_name',
#                                              'svr_lan_ip',
#                                              'svr_rack_name',
#                                              'svr_pos_id',
#                                              'svr_raid_type']].sort_values(by=['svr_rack_name',
#                                                                                'svr_pos_id']).to_string())


# 按机柜统计服务器数量
# print(df['svr_rack_name'].value_counts())

# 已使用的机柜情况
print(df['svr_rack_name'].dropna().unique())

