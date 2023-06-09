# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/23 17:02
 Tool  : PyCharm
"""

# 使用requests.utils.cookiejar_from_dict()方法，将一个字典直接转为RequestsCookieJar对象

# import requests
#
# url = "http://httpbin.org/cookies"
#
# cookies = {"name": "xialaodi"}
#
# jar = requests.utils.cookiejar_from_dict(cookies)
#
# r = requests.get(url, cookies=jar)
#
# print(r.text)

# 构造一个RequestsCookieJar对象

# import requests
#
# url = "http://httpbin.org/cookies"
#
# jar = requests.cookies.RequestsCookieJar()
#
# jar.set("name", "xialaodi", domain="httpbin.org", path="/cookies")
#
# r = requests.get(url, cookies=jar)
#
# print(r.text)


# 使用request.utils.add_dict_to_cookiejar()方法，继续向RequestsCookieJar对象中添加cookie
import requests

url = "http://httpbin.org/cookies"

cookies = {"name": "xialaodi"}

jar = requests.utils.cookiejar_from_dict(cookies)

r = requests.get(url, cookies=jar)

print(r.text)

# 构造一个字典变量，并通过add_dict_to_cookiejar方法加到之前的cookie变量中
new_cookies = {"password": "123456"}
requests.utils.add_dict_to_cookiejar(jar, new_cookies)

r = requests.get(url, cookies=jar)
print(r.text)
