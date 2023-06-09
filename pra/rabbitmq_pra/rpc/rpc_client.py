#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/21 11:17
@Author  : Jason
@Site    : 
@File    : rpc_client.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import uuid


class FibonacciRpcClient(object):

    # 初始化：
    # 建立连接，设置接收队列信息
    def __init__(self):
        # 建立连接
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.216.3'))

        self.channel = self.connection.channel()

        # 获取系统分配的队列名称
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        # 设置系统分配的队列为接收消息的队列
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    # 调用函数：处理从rpc_server返回的信息
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    # 发送消息
    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n).encode(encoding='utf-8'))
        self.connection.process_data_events(time_limit=None)
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)
