#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/20 11:12
@Author  : Jason
@Site    : 
@File    : new_task.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import sys

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3', port=5677))
# 获取channel
channel = connection.channel()

# 声明队列信息
# channel.queue_declare(queue='task_queue', durable=True)
channel.queue_declare(queue='tt_mirror', durable=True)

# 创造消息
for num in range(20):
    message = ' '.join(str(num)) + '.' * num
# message = ' '.join(sys.argv[1:]) or "Hello World!"
# message = 'hello.world.hi.get..'

# 执行消息发布的exchange为默认，队列为 task_queue
    channel.basic_publish(
        exchange='',
        routing_key='tt_mirror',
        body=message.encode(encoding='utf-8'),
        # 指定发布的消息需要持久化
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(" [x] Sent %r" % message)
connection.close()
