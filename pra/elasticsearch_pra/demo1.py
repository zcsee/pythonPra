#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/1 10:23
@Author  : Jason
@Site    : 
@File    : demo1.py
@Project : leetcode
@Software: PyCharm
"""
from elasticsearch import Elasticsearch

# es = Elasticsearch()    # 默认连接本地elasticsearch
# es = Elasticsearch(['127.0.0.1:9200'])  # 连接本地9200端口
es = Elasticsearch(
    ["http://192.168.216.3:9200", "http://192.168.216.3:9201", "http://192.168.216.3:9202", "http://192.168.216.3:9203",
     "http://192.168.216.3:9204"])

# 插数据进py3，并查询
# print(es.index(index='py3', id='1', document={'name': "张开", "age": 18}))
# print(es.get(index='py3', id='1'))

reps = es.info().body
print(f"{reps['name'] =}")
