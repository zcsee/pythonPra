#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/17 17:42
@Author  : Jason
@Site    : 
@File    : sender.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import json

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明队列
channel.queue_declare(queue='hello')

dict1 = {"消息内容": "bar"}
# 通过默认值为空字符串的exchange，通过routing_key指定队列名为‘hello’，进行消息发送
# The queue name needs to be specified in the routing_key parameter:
# channel.basic_publish(exchange='', routing_key='hello', body=b'Hello World!')
channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(dict1).encode(encoding='utf-8'))

# 发送完打印提示
print(" [x] Sent 'Hello World!'")

# 关闭连接
connection.close()
