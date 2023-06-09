#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/21 10:08
@Author  : Jason
@Site    : 
@File    : receive_logs_topic.py
@Project : leetcode
@Software: PyCharm
"""
import time

import pika
import sys

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明exchange名称为 topic_logs，类型为 topic
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# channel.basic_qos(prefetch_count=1)

# 声明队列名称为系统分配，自动删除
result = channel.queue_declare('', exclusive=True)
# 获取系统分配到的队列名
queue_name = result.method.queue

# 指定绑定名称
# binding_keys = sys.argv[1:]
binding_keys = input("Please input binding_keys: ").split(' ')

print(f"{binding_keys=}")
# 判断binding_keys是否正确
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

# 根据每个binding_keys建立exchange和queue的绑定关系
for binding_key in binding_keys:
    print(f"{binding_key=}")
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


# 指定回调函数，打印routing_key和消息体
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    time.sleep(0.1)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 接收消息的配置，自动确认
channel.basic_consume(
    queue=queue_name, on_message_callback=callback)

# 开始接收消息
channel.start_consuming()
