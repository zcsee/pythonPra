# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/3 17:48
 Tool   : PyCharm
 Content: 
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


so = Solution()
res = so.jump([2, 3, 1, 1, 4])
print(f"{res=}")
