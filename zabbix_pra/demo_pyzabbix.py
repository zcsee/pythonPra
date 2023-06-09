# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/9 5:00
 Tool   : PyCharm
 Content: 
"""

from pyzabbix import ZabbixAPI

ZABBIX_SERVER = 'http://192.168.30.128'

zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login('Admin', 'zabbix')

host_list = zapi.host.getMessage(output="extend", )
for host in host_list:
    print(f'{host["hostid"]=}')
