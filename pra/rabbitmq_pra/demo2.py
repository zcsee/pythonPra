#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/17 16:18
@Author  : Jason
@Site    : 
@File    : demo1.py
@Project : leetcode
@Software: PyCharm
"""
import pika  # 安装pika模块连接mq
import json
import os
import threading


# 项目基本配置
class BaseConfig():
    env = os.environ.get('env', 'sit')  # 获取环境变量


# rabbitmq 配置信息
class RabbitMQConfig(object):
    if BaseConfig.env in ['dev', 'sit']:
        host = "192.168.216.3"
        port = 5672
        username = "admin"
        password = "123"
        vhost = f"hello_mq_{BaseConfig.env}"
        exchange = f"hello_mq_{BaseConfig.env}"
        routing_key = f"hello_mq_{BaseConfig.env}"
        queue_name = f"hello_mq_{BaseConfig.env}"

    if BaseConfig.env in ['prod', ]:
        pass


# 消费者消费时basic_consume函数中的on_message_callback参数会执行此方法，我们Python程序进而在这里可以拿到消息内容 和 给rabbitmq回调ack
def callback(ch, method, properties, body):
    print('callback body ', body.decode(encodings='utf-8'))  # 在这里对消息内容进行我们想做的处理
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动应答ack，确保消息真正消费后才应答


class RabbitMQ(object):
    def __init__(self, username, password, host, port, virtual_host):
        self.channel = None
        self.connect = None
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.virtual_host = virtual_host
        self.get_connect()  # 初始化RabbitMQ实例对象时完成连接rabbitmq服务器

    def get_connect(self):
        credentials = pika.PlainCredentials(username=self.username, password=self.password)  # 登录凭证
        self.connect = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, virtual_host=self.virtual_host,
                                      credentials=credentials))
        self.channel = self.connect.channel()  # 客户端连接rabbitmq服务端后开辟管道，每个channel代表一个会话任务
        # self.channel.basic_qos(1)

    def produce(self, exchange, routing_key, queue, body):
        # 创建exchange消息交换机， 并且exchange持久化
        self.channel.exchange_declare(
            exchange=exchange,
            exchange_type='direct',
            durable=True)
        # 声明队列， 并且队列持久化
        self.channel.queue_declare(queue=queue, durable=True)
        # 通过routing_key 绑定 消息交换机和队列
        self.channel.queue_bind(queue, exchange, routing_key)
        # 发消息
        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,  # 根据exchange和routing进而指定 队列
            body=body,  # 发送的数据
            properties=pika.BasicProperties(delivery_mode=2)  # 消息持久化存到硬盘， 1是非持久化
        )

    def getMessage(self, exchange, queue, callback):
        print('消费任务启动')
        self.channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)
        self.channel.queue_declare(queue=queue, durable=True)
        self.channel.basic_consume(
            queue=queue,  # 队列名
            on_message_callback=callback,  # 指定回调函数
            auto_ack=False,  # 关闭自动ack采用手动应答
        )
        self.channel.start_consuming()  # 开始接收信息，并进入阻塞状态，队列里有信息才会调用on_message_callback进行处理


if __name__ == "__main__":

    # 将要发送的消息
    a = {
        "消息内容": "message",
    }

    # 实例化的rabbbitmq对象
    rabbit_obj = RabbitMQ(username=RabbitMQConfig.username,
                          password=RabbitMQConfig.password,
                          host=RabbitMQConfig.host,
                          port=RabbitMQConfig.port,
                          virtual_host=RabbitMQConfig.vhost)

    # 发消息
    for i in range(1):
        rabbit_obj.produce(RabbitMQConfig.exchange, RabbitMQConfig.routing_key, RabbitMQConfig.queue_name,
                           json.dumps(a).encode(encoding='utf-8'))
        print('生产者发送第 {} 个消息成功 '.format(i))

    # 开子线程 去监听消费消息
    # p = threading.Thread(target=rabbit_obj.get, args=(RabbitMQConfig.exchange, RabbitMQConfig.queue_name, callback,))
    # p.start()

    # print('\n -- 主程序不被阻塞，执行其它操作 --- \n')
