#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/21 11:17
@Author  : Jason
@Site    : 
@File    : rpc_server.py
@Project : leetcode
@Software: PyCharm
"""
import pika

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3'))
channel = connection.channel()

# 声明队列
channel.queue_declare(queue='rpc_queue')


# 定义费布那切函数
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# 定义回调函数
def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    # 发消息到reply_to指定的queue，指定correlation_id
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    # 手动确认
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 限定每次只接收一个
channel.basic_qos(prefetch_count=1)
# 设置接收的队列为 rpc_queue，回调函数为 on_request
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
# 开始接收消息
channel.start_consuming()
