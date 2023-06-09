# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 12:56
 Tool   : PyCharm
 Content: 两数相除：给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
"""

nums = [[1,2,3],[1,3,2]]

nums1 = [1,3,2]
nums2 = [1,2,3]
if nums1.sort() == nums2.sort():
    print("相等")