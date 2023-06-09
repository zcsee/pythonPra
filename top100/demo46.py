# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/4 16:49
 Tool   : PyCharm
 Content: 全排列
 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(sol,nums, check):
            if len(sol) == n:
                res_lst.append(sol[:])
                return

            for i in range(n):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue

                check[i] = 1
                backtrack(sol + [nums[i]], nums, check)
                check[i] = 0

        nums.sort()
        res_lst = []
        n = len(nums)
        check = [0 for _ in range(len(nums))]
        backtrack([], nums, check=check)
        return res_lst


so = Solution()
ans = so.permute([1, 1, 2])
print(f'{ans=}')
