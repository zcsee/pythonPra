# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/11/30 14:51
 Tool   : PyCharm
 Content: 模拟百度搜索
"""
import urllib.parse
from urllib import request

# 构造url
url = "https://www.baidu.com"
word = {"wd": "上海"}
# 通过parse转成url编码格式
word = urllib.parse.urlencode(word)
new_url = url + "?" + word

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

request = urllib.request.Request(new_url, headers=headers)
response = urllib.request.urlopen(request)

# 将response中的信息读出来，并解码
html = response.read().decode(encoding='utf-8')

print(html)
