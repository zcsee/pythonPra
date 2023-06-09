# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/27 11:05
 Tool   : PyCharm
 Content: 
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        res_lst = []
        n = len(prices)
        for i in range(1, n):
            res_lst.append(max(0, prices[i] - prices[i - 1]))
        if len(res_lst) >= 2:
            res_lst.sort()
            result = res_lst[-1] + res_lst[-2]
        else:
            result = res_lst[:]
        return result


so = Solution()
res = so.maxProfit([1, 2, 3, 4, 5])
print(f"{res=}")
