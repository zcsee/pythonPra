# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 11:40
 Tool   : PyCharm
 Content: 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)

        while (nums.count(val)) > 0 and  (inx := nums.index(val)) is not None:
            nums.pop(inx)
            length -= 1
        return length


so = Solution()
res = so.removeElement([3,2,2,3],3)
print(f"{res}")