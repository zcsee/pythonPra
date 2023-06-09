# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/11 11:58
 Tool   : PyCharm
 Content: 爬楼梯
 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        dp = [0 for _ in range(n)]

        dp[1] = 1
        dp[2] = 2

        for i in range(3,n):
            dp[i] = dp[i-2] + dp[i -1 ]
        # 返回第n阶台阶
        return dp[n-1]+dp[n-2]


so = Solution()
ans = so.climbStairs(5)
print(f"{ans=}")
