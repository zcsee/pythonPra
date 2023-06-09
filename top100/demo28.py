# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 12:45
 Tool   : PyCharm
 Content: 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length_needle = len(needle)
        length_haystack = len(haystack)

        hash_needle = hash(needle)
        tmp_str_lst = []
        if not length_needle:
            return 0
        for inx in range(length_haystack - length_needle + 1):
            tmp_str_lst.append(hash(haystack[inx:inx+length_needle]))
        length_tmp = len(tmp_str_lst)
        print(tmp_str_lst)
        for i in range(length_tmp):
            if tmp_str_lst[i] == hash_needle:
                return i

        res_num = -1
        return res_num


so = Solution()
res = so.strStr('abdcd','cd')
print(f'{res=}')
