# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/25 23:57
 Tool   : PyCharm
 Content: 给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
        请你找出所有和为 0 且不重复的三元组。
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()

        length = len(nums)
        inx_r = length - 1

        res_lst = []

        for inx in range(length - 2):
            if nums[inx] > 0:
                break
            if inx > 0 and nums[inx] == nums[inx - 1]:
                continue
            inx_l = inx + 1
            inx_r = length - 1
            while inx_l < inx_r:
                sum = nums[inx] + nums[inx_l] + nums[inx_r]
                if sum == 0:
                    res_lst.append([nums[inx], nums[inx_l], nums[inx_r]])
                if sum < 0:
                    # 当三数之和小于0，左指针右移
                    inx_l += 1
                    while inx_l < inx_r and  nums[inx_l] == nums[inx_l-1]:
                        inx_l += 1
                else:
                    # 否则右指针左移
                    inx_r -= 1
                    while inx_l < inx_r and  nums[inx_r] == nums[inx_r + 1]:
                        inx_r -= 1
        return res_lst


so = Solution()
result = so.threeSum([-2,0,1,1,2])
print(result)