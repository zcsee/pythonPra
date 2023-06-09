# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 13:45
 Tool   : PyCharm
 Content: 
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romon_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i != len(s) - 1 and romon_dic.get(s[i]) < romon_dic.get(s[i + 1]):
                res -= romon_dic.get(s[i])
            else:
                res += romon_dic.get(s[i])
        return res
