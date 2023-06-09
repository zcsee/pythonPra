# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 14:18
 Tool   : PyCharm
 Content: 查找字符串数组中的最长公共前缀
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        inx = 0
        tmp_char = ''
        res_str = ''
        i = 0
        tmp_set = set()
        while i < length:
            # if i != length -1 and strs[i][inx] == strs[i+1][inx]:
            #     tmp_char = strs[i][inx]
            #     i += 1
            #
            tmp_set.add(strs[i][inx])
            if i == length - 1 and len(tmp_set) == 1:
                res_str += strs[i][inx]
                i = 0
                inx += 1
                tmp_set.clear()
                continue
            if len(tmp_set) != 1:
                break
            i += 1
        print(res_str)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ''
        inx, count = len(strs[0]), len(strs)
        for i in range(inx):
            c = strs[0][i]
            if any(i == len(strs[j]) or c != strs[j][i] for j in range(1, count)):
                return strs[0][:i]

        return strs[0]


so = Solution()
so.longestCommonPrefix2(["flower", "flow", "flight"])
