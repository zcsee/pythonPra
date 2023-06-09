# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 13:55
 Tool   : PyCharm
 Content: 最大子数组和
 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 获取数组长度
        n = len(nums)
        # 构建用于记录子数组和的数组
        dp = [0 for _ in range(n)]
        # 第一个子数组和为单元素，所以直接赋值，不用计算
        dp[0] = nums[0]

        for i in range(1,n):
            if dp[i-1]>0:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)


so = Solution()
res = so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(f"{res=}")
