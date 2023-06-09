# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/16 14:21
 Tool   : PyCharm
 Content: 交错字符串
 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        res_bool = False

        # 获取三个字符串的长度
        len_1 = len(s1)
        len_2 = len(s2)
        len_3 = len(s3)

        # 如果s1 + s2的长度不等于S3的，则直接返回False
        if len_1 + len_2 != len_3:
            return False

        # 构造二维数组，默认值为False
        dp = [[False] * (len_2 + 1) for _ in range(len_1 + 1)]
        dp[0][0] = True

        # 设置初始的数组
        for i in range(1, len_1 + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for i in range(1, len_2 + 1):
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])

        for i in range(1, len_1 + 1):
            for j in range(1, len_2 + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]


so = Solution()
res_bool = so.isInterleave("aa", "dc", "adbc")
print(f"{res_bool=}")
