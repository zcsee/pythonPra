# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/23 14:20
 Tool  : PyCharm
"""

import requests
import json

# r = requests.get(url='https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# print(r)
# print(f"返回的r类型为:{type(r)}")
#
# # 返回的状态码
# print(f"返回的状态码为:{r.status_code}")
#
# # 获取header信息
# print(f"整个header为:{r.headers}")
# print(f"获取header中的content-type部分:{r.headers['content-type']}")
# print(f"获取header中的Connection部分:{r.headers['Connection']}")
# print(f"获取返回的文本:{r.text},类型为{type(r.text)}")
# print(f"获取返回的文本(content):{r.content.decode(encoding='utf-8')},类型为{type(r.content)}")
# print(f"获取返回的编码:{r.encoding}")
# print(f"以json格式返回页面结果:{r.json()},类型为{type(r.json())}")
# print(f"获取cookie:{r.cookies.get_dict()},类型为{type(r.cookies)}")


r2 = requests.post(url='https://httpbin.org/post', data={"name": "jason"}, headers={"accept": "application/json"})
print(r2.status_code)
print(r2.headers)
print(r2.text)


with open('test_json.json','w') as fd:
    fd.write(r2.text)
