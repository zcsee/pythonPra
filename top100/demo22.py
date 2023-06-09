# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/29 9:45
 Tool   : PyCharm
 Content: 括号生成
 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
from functools import lru_cache
from typing import List


class Solution:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']

        ans = []

        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append(f'({left}){right}')
        return ans


so = Solution()
res = so.generateParenthesis(2)
print(res)
