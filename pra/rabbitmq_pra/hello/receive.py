#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/17 17:43
@Author  : Jason
@Site    : 
@File    : receive.py
@Project : leetcode
@Software: PyCharm
"""
import os
import pika
import sys


def main():
    # 连接rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.216.3'))
    channel = connection.channel()

    # 声明队列名
    channel.queue_declare(queue='hello')

    # 定义一个回调函数，功能为打印接收的消息的主体
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        print(body.decode(encoding='gb2312'))

    # 指定回调函数和自动确认
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    # 打印准备接收的提示
    print(' [*] Waiting for messages. To exit press CTRL+C')

    # 开启一个阻塞进程，进行消息接收
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
