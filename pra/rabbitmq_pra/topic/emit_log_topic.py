#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/21 10:08
@Author  : Jason
@Site    : 
@File    : emit_log_topic.py
@Project : leetcode
@Software: PyCharm
"""
import random

import pika
import sys

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明exchange名为 topic_logs，类型为 topic
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# 随机关键词
key_words = ['lazy', 'orange', 'green', 'rabbit']

# 发送消息时指定exchange，routing_key和消息内容
for i in range(10000):
    routing_key = key_words[random.randint(0, 3)]
    for _ in range(2):
        routing_key += '.' + key_words[random.randint(0, 3)]
    # routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
    # message = ' '.join(sys.argv[2:]) or 'Hello World!'
    message = 'hello'
    channel.basic_publish(
        exchange='topic_logs', routing_key=routing_key, body=message.encode(encoding='utf-8'))
    print(" [x] Sent %r:%r" % (routing_key, message))

connection.close()
