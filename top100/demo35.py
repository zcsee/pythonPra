# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/1 15:00
 Tool   : PyCharm
 Content: 搜索插入位置
 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length_nums = len(nums)

        l, r = 0, length_nums - 1
        if target <= nums[l]:
            return 0
        if target > nums[r]:
            return r + 1
        mid = -1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if nums[mid] < target and target != nums[mid + 1]:
            mid += 1
        return mid


so = Solution()
res_inx = so.searchInsert([1, 3], 3)
print(f"{res_inx=}")


# nus = [1,3,5,6]
# nus.insert(3,4)
# print(f"{nus=}")