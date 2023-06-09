# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/15 10:51
 Tool   : PyCharm
 Content: 长度最小的子数组
 给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start = end = 0
        total = 0

        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans


so = Solution()
res_bool = so.minSubArrayLen(7, [2, 3, 4, 1, 2, 4, 3])
print(f"{res_bool=}")
