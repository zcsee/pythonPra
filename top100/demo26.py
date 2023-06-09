# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 11:25
 Tool   : PyCharm
 Content: 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res_length = 0
        if len(nums) == 1:
            return 1
        inx = 0
        while inx < len(nums) -1:
            if nums[inx] == nums[inx + 1]:
                nums.pop(inx)
                # continue
            else:
                inx += 1
        res_length = len(nums)
        return res_length


so = Solution()
res = so.removeDuplicates([0,1,2,2,3,3,4,5,6,6])
print(f'{res=}')
