# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/12 11:23
 Tool   : PyCharm
 Content: 删除有序数组中的重复项II
 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def solve(k):
            u = 0
            for x in nums:
                if u < k or nums[u - k] != x:
                    nums[u] = x
                    u += 1
            return u

        return solve(2)


so = Solution()
res = so.removeDuplicates([0, 1, 1, 1, 3, 3, 3, 3])
print(f"{res=}")
