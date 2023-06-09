#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/3 11:25
@Author  : Jason
@Site    : 
@File    : convert_json_from_bson.py
@Project : leetcode
@Software: PyCharm
"""
import bson

with open('./y.bson', 'rb') as f:
    coll_raw = f.read()

coll = bson.decode_all(coll_raw)
