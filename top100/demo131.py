# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/29 15:24
 Tool   : PyCharm
 Content: 分割回文串
 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
回文串 是正着读和反着读都一样的字符串
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [[True] * n for _ in range(n)]

        # 动态规划
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]

        ret = list()
        ans = list()

        def dfs(i : int):
            if i == n:
                ret.append(ans[:])
                return

            for j in range(i,n):
                if f[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j+1)
                    ans.pop()

        dfs(0)
        return ret


so = Solution()
res_lst = so.partition("aaba")
print(f"{res_lst=}")
