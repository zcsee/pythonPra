# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/9 15:50
 Tool   : PyCharm
 Content: 
"""
import json
import urllib.request


def get_response_dic(data):
    url = 'http://192.168.30.128/api_jsonrpc.php'
    header = {'Content-Type': 'application/json'}
    data = bytes(data, 'utf-8')
    request = urllib.request.Request(url, data, header)
    response = urllib.request.urlopen(request)
    result_str = response.read().decode('utf-8')
    result_dic = json.loads(result_str)
    return result_dic


def get_result(raw):
    data = json.dumps(raw)
    result = get_response_dic(data)
    return result


def get_auth():
    raw = {"jsonrpc": "2.0", "method": "user.login", "params": {"user": "Admin", "password": "zabbix"}, "id": 0}  # 提交数据
    data = json.dumps(raw)
    auth = get_response_dic(data)['result']
    return auth


def get_host_list(auth):
    raw = {
        "jsonrpc": "2.0",
        "method": "hostinterface.get",
        "params": {
            "output": "extend",
            # "hostids": "30057"
        },
        "auth": auth,
        "id": 1
    }
    host_list_dic = get_result(raw)
    return host_list_dic['result']


def creat_host(auth, hostid, ip, dns='', main_host=0, port='10050', type_host=1, useip=1):
    # raw = {
    #     "jsonrpc": "2.0",
    #     "method": "hostinterface.create",
    #     "params": {
    #         "hostid": "30052",
    #         "dns": "",
    #         "ip": "127.0.0.1",
    #         "main": 0,
    #         "port": "10050",
    #         "type": 1,
    #         "useip": 1
    #     },
    #     "auth": auth,
    #     "id": 1
    # }
    raw = {
        "jsonrpc": "2.0",
        "method": "hostinterface.create",
        "params": {
            "hostid": hostid,
            "dns": dns,
            "ip": ip,
            "main": main_host,
            "port": port,
            "type": type_host,
            "useip": useip
        },
        "auth": auth,
        "id": 1
    }


def update_host_port(auth, host_port, hostid, host_type=1):
    raw = {
        "jsonrpc": "2.0",
        "method": "hostinterface.update",
        "params": {
            "interfaceid": hostid,
            "port": host_port
        },
        "auth": auth,
        "id": 1
    }
    result = get_result(raw)
    return result


def main():
    auth = get_auth()
    print(auth)
    host_list = get_host_list(auth)
    print(host_list)
    # creat_host(auth, hostid='10318', ip='192.168.7.7', type_host=1)
    result = update_host_port(auth, hostid='10318', host_port=30050)
    print(result)


if __name__ == '__main__':
    main()
