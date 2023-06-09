# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/23 10:34
 Tool  : PyCharm
"""

import json


# 将python的 字典对象 转成 字符串类型
person = {"name": 'jason', 'age': 30, "phone_no": ["55779087", "18682266706"], "isOnly": True}
print(type(person), person)

# 通过json.dumps()方法，实现字典向字符串的转化
jsonStr = json.dumps(person)
print(type(jsonStr), jsonStr)

# 通过json.dump()函数，实现将字典转换成字符串，并写入到指定文件中
with open("test_json.json", "w") as fd:
    json.dump(person, fd)
