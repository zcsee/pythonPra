#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/20 11:13
@Author  : Jason
@Site    : 
@File    : work.py
@Project : leetcode
@Software: PyCharm
"""
import pika
import time

# 建立连接
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.216.3', port=5677))
# 获取channel
channel = connection.channel()

# 声明队列，设置持久化
channel.queue_declare(queue='tt_mirror', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


# 定义回调函数，并按照 . 的数量进行休眠，最后手动ack
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    # 手动ack，确保任务处理完成再进行确认
    ch.basic_ack(delivery_tag=method.delivery_tag)


'''
This uses the basic.qos protocol method to tell RabbitMQ not to give more than one message to a worker at a time
in other words, don't dispatch a new message to a worker until it has processed and acknowledged the previous one.
Instead, it will dispatch it to the next worker that is not still busy.
'''
channel.basic_qos(prefetch_count=1)

# 指定接收消息的队列为‘task_queue’，回调函数为callback
channel.basic_consume(queue='tt_mirror', on_message_callback=callback)

# 开始接收消息
channel.start_consuming()
