# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/24 11:34
 Tool  : PyCharm
 lib   : StrictRedis 库
 Content: 系统相关变量和操作
"""

import redis
from redis import StrictRedis

# 两种使用StrictRedis连接redis数据库的方式
# s = StrictRedis.from_url('redis://192.168.216.3/test')
# 推荐
s = StrictRedis(host='192.168.216.3', port=6379, db=0, decode_responses=True)

# 获取所有的key，返回一个列表
keys = s.keys()
print(f"{keys =}")

# 通过scan，返回一个元组
keys1 = s.scan()
print(f"{keys1 =}")

# 通过scan_iter返回一个迭代器
keys2 = s.scan_iter()
print(f"{keys2 =}")

count = 0
for key in keys2:
    print(key)
    count += 1
print(count)

# 获取string类型的值
print(f"{s.get('t_string') = }")

# 获取list类型的值
print(f"{s.lrange('t_list',0,-1) = }")
# 在list中插入一个值，返回该list的长度
# print(f"{s.lpush('t_list',100)}")


# 获取hash类型的值
print(f"{s.hget('t_hash',key='t') = }")
print(f"{s.hgetall('t_hash')}")

# 获取set类型的值
print(f"{s.smembers('t_set') = }")
