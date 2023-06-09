#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/20 17:28
@Author  : Jason
@Site    : 
@File    : emit_log_direct.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import sys

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明exchange名称为direct_logs，类型为direct
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 创造消息：严重级别和消息内容
for i in range(20):
    if i % 2 == 0:
        severity = 'info'
        message = 'save'
    else:
        severity = 'critical'
        message = 'gg'
# severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
# message = ' '.join(sys.argv[2:]) or 'Hello World!'

    # 指定exchange和routing_key，开始发送消息
    channel.basic_publish(
        exchange='direct_logs', routing_key=severity, body=message.encode(encoding='utf-8'))

    print(" [x] Sent %r:%r" % (severity, message))

connection.close()
