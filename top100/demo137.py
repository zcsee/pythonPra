# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/5 14:27
 Tool   : PyCharm
 Content: 只出现一次的数字2
 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素
"""
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        # print(f"{freq=}")
        ans = [num for num, occ in freq.items() if occ == 1][0]
        # for num,occ in freq.items():
        #     print(f"{num=},{occ=}")
        return ans

so = Solution()
ans_s = so.singleNumber([2,3,2,2])
print(f"{ans_s=}")