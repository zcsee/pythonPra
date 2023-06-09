# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/1 11:46
 Tool   : PyCharm
 Content: 在排序数组中查找元素的第一个和最后一个位置
 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""
from typing import List


class Solution:
    # 查找左边界
    def leftMargin(self, nums: List[int], target: int):

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # 如果 nums[mid] = target，继续向左寻找左边界
            if nums[mid] >= target:
                high = mid - 1
            # elif nums[mid] > target:
            #     high = mid - 1
            else:
                low = mid + 1
        if nums[low] == target:
            return low
        # 如果左边界的值不等于 target
        else:
            return -1

    # 寻找右边界
    def rightMargin(self, nums: List[int], target: int):

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # 如果 nums[mid] = traget，继续向右寻找右边界
            if nums[mid] == target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        if nums[high] == target:
            return high
        # 如果右边界的值不等于 target
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        lm = self.leftMargin(nums, target)
        rm = self.rightMargin(nums, target)

        return [lm, rm]


so = Solution()
res_lst = so.searchRange([5, 7, 7, 8, 8, 8, 10], 8)
print(f"{res_lst=}")
