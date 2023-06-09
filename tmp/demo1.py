#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/16 15:55
@Author  : Jason
@Site    : 
@File    : demo1.py
@Project : leetcode
@Software: PyCharm
"""


def cal_i_j_k():
    for i in range(2000):
        for j in range(2000):
            for k in range(2000):
                if i * j + k == 2020 and i + j * k == 2021:
                    print(f"{i=},{j=},{k=}")
                    break
                    # print("hehe")


if __name__ == "__main__":
    cal_i_j_k()
