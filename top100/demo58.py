# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 16:16
 Tool   : PyCharm
 Content: 最后一个单词的长度
 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # res_len = 0
        # s = s.strip()
        s = s.strip().split(sep=' ')
        return len(s[-1])
        # print(f"{s=}")


so = Solution()
s_len = so.lengthOfLastWord("   fly me   to   the moon  ")
print(f"{s_len=}")
