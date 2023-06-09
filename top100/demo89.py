# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/13 13:59
 Tool   : PyCharm
 Content: 格雷编码
 n 位格雷码序列 是一个由 2n 个整数组成的序列，其中：
每个整数都在范围 [0, 2n - 1] 内（含 0 和 2n - 1）
第一个整数是 0
一个整数在序列中出现 不超过一次
每对 相邻 整数的二进制表示 恰好一位不同 ，且
第一个 和 最后一个 整数的二进制表示 恰好一位不同
给你一个整数 n ，返回任一有效的 n 位格雷码序列
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]

        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << i - 1))
        return ans


so = Solution()
res = so.grayCode(4)
print(f"{res=}")
