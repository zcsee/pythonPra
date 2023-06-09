#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
参考:http://kazoo.readthedocs.io/en/latest/basic_usage.html#creating-nodes
"""

from kazoo.client import KazooClient

# Create a client and start it
zk = KazooClient(hosts='172.16.1.137:2183', timeout=5)
zk.start()

# Now you can do the regular zookeeper API calls
# Ensure some paths are created required by your application
ensure_result = zk.ensure_path("/redis_t/group1")
print(ensure_result)

# watchers
# @zk.ChildrenWatch('/mysql/host')
# def mysql_watcher(children):
#     print('/mysql/host changed :%s'%children)


# 获取指定节点的值
# print(zk.get('/mysql/host',watch=mysql_watcher2))
# print(zk.get('/mysql/port',watch=None))
# print(zk.get('/mysql/user',watch=None))
# print(zk.get('/mysql/pwd',watch=None))

'''
Reading Data
Methods:
    exists()
    get()           获取key对应的value值
    get_children()  获取节点下的key信息
'''
# Determine if a node exists
if zk.exists("/redis_t/group1"):
    # Do something
    # print(zk.get_children('/redis_t/group1'))
    print(zk.getMessage('/redis_t/group1'))
else:
    print("/redis_t/group1 doesn't exists!")

'''
Creating Nodes
Methods:
    ensure_path()   插入节点
    create()        创建节点key,value
'''
# zk.ensure_path('/mysql/test')
# zk.create('/mysql/test/node',b'node value')

'''
Updating Data
Methods:
    set()
'''
# zk.set('/mysql/test/node',b'value')
# print(zk.get('/mysql/test/node'))

'''
Deleting Nodes
Methods:
    delete()
'''
# zk.delete('/mysql/test', recursive=True)

# In the end, stop it
zk.stop()
zk.close()
