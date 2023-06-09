#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/20 17:02
@Author  : Jason
@Site    : 
@File    : receive_logs.py
@Project : leetcode
@Software: PyCharm
"""
import pika

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明exchange名称为logs，类型为fanout
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 声明队列名称为系统分配，进程断开后，队列删除
result = channel.queue_declare(queue='', exclusive=True)
# 获取系统分配的队列的名称
queue_name = result.method.queue

# 设置exchange和queue的绑定
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


# 回调函数，设置为打印接收到的消息
def callback(ch, method, properties, body):
    print(" [x] %r" % body.decode())


# 设置消费的参数，指定队列名和回调函数，自动确认
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

# 开始接收信息
channel.start_consuming()
