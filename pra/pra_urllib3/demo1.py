# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/9 15:17
 Tool   : PyCharm
 Content: 
"""
import urllib.request
import urllib.parse
import json

# 指定url
url = 'http://192.168.30.128/api_jsonrpc.php'  # 提交到表单页面

# 指定header
header = {'Content-Type': 'application/json'}

# 构造data
raw = {"jsonrpc": "2.0", "method": "user.login", "params": {"user": "Admin", "password": "zabbix"}, "id": 0}  # 提交数据
data = json.dumps(raw)
data = bytes(data, 'utf-8')

# 构造request请求，将上面的url、header和data组合在一起
request = urllib.request.Request(url, data, header)  # 请求处理
# print(request.data)

# 获取返回值
response = urllib.request.urlopen(request)  # 读取结果

# 打印返回值
result_str = response.read().decode('utf-8')
result_dic = json.loads(result_str)


print(response.cookies)
# print(type(result_dic))

# 取出auth
auth = result_dic['result']
print(result_dic['result'])

