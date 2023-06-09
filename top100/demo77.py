# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/11 16:34
 Tool   : PyCharm
 Content: 组合
 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
你可以按 任何顺序 返回答案
"""
import math
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(n, k, startIndex):
            # 回溯结束条件：path中包含的元素数量为指定的长度
            if k == len(path):
                result.append(path[:])
                return
            # 通过指定startIndex，进行元素模拟，默认从1开始，到n结束
            # n - (k - len(path)) + 1 为元素下标，需要加1得到真实的元素值
            for i in range(startIndex, n - (k - len(path)) + 1 + 1):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()

        backtracking(n, k, 1)
        return result


so = Solution()
l_lst = so.combine(5,2)
print(f"{l_lst=}")
