#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/20 17:29
@Author  : Jason
@Site    : 
@File    : receive_logs_direct.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import sys

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# 声明队列，并获取系统分配的队列名称
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 指定严重级别
# severities = sys.argv[1:]
# severities = ['info', 'critical']
# 只接收info级别的
severities = ['info']
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# 每个严重级别设定一个routing_key，绑定到上面的队列
for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


# 回调函数
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


# 开始接收消息，自动ack
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
