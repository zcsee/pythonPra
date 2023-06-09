# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/13 14:07
 Tool   : PyCharm
 Content: 子集
 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        # 计算数组长度
        n = len(nums)

        def dfs(ns, start_index):
            ans.append(path[:])
            for i in range(start_index, n):
                # 同树层去重
                if i > start_index and nums[i] == nums[i - 1]:
                    continue

                # 添加新元素
                path.append(nums[i])
                # 用新元素进行往下一层树层查找
                dfs(nums, i + 1)
                # 回溯到之前的状态
                path.pop()

        dfs(nums, 0)
        return ans

so = Solution()
res = so.subsetsWithDup([1, 2, 3])
print(f"{res=}")
