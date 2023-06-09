#! /usr/bin/python
# -*- coding: UTF-8 -*-

# 获得iterator对象
it = iter([1, 2, 3, 4, 5])
# 循环
while True:
    try:
        # 获取下一个值
        x = next(it)
        print("x's value is: {}.".format(x))
    except StopIteration:
        # 遇到StopIteration异常就退出
        break
