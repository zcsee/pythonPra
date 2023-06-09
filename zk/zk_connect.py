from kazoo.client import KazooClient

zk = KazooClient(hosts='172.16.1.137:2181')
zk.start()
zk.stop()
zk.close()