# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/23 17:07
 Tool  : PyCharm
"""
import requests

# 获取session对象
s = requests.Session()
# 设置url
url = "http://httpbin.org/cookies/set/age/20"
# 通过session去访问url
r = s.get(url)

# 打印返回的结果
print("第一次访问============")
print(r.text)
# 查看session中cookie的值
print(s.cookies)

# 构造新的url
url = "http://httpbin.org/cookies"
# 使用同一个session进行url访问
r = s.get(url)
print("第二次访问============")
print(r.text)
# 查看session中cookie的值
print(s.cookies)

# 使用同一个session进行url访问，并设置新的cookie,临时生效，后续在session中的cookie不继续生效
r = s.get(url, cookies={"password": "123456"})
print("第三次访问============")
print(r.text)
# 查看session中cookie的值
print(s.cookies)

# 在第三次访问的基础上，去除掉cookie的传参
r = s.get(url)
print("第四次访问============")
print(r.text)

# 查看session中cookie的值
print(s.cookies)
