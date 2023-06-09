#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/20 17:01
@Author  : Jason
@Site    : 
@File    : emit_log.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import sys

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
# 获取通道
channel = connection.channel()

# 声明exchange为logs，类型为fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')

for num in range(10):
    # 创造消息
    # message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    message = '+'.join(str(num) + " " + str(num)) + '.' * num
    # 开始发送消息
    channel.basic_publish(exchange='logs', routing_key='', body=message.encode(encoding='utf-8'))
    print(" [x] Sent %r" % message)
connection.close()
