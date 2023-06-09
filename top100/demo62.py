# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 20:27
 Tool   : PyCharm
 Content: 不同路径
 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径
"""
from math import comb


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]

    def uniquePaths2(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

so = Solution()
ans = so.uniquePaths2(4, 9)
print(f"{ans=}")
