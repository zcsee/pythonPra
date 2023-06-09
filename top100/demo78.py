# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/12 10:16
 Tool   : PyCharm
 Content: 子集
 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集
"""
import itertools
from typing import List


class Solution:
    # 库函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(n + 1):
            for tmp in itertools.combinations(nums,i):
                result.append(list(tmp))
        return result

    # 迭代
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    # 回溯
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]])

        helper(0, [])
        return res


so = Solution()
nn = so.subsets2([1,2,3])
print(f"{nn=}")
