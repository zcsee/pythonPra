# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 13:32
 Tool   : PyCharm
 Content: 下一个排列
 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = -1
        length = len(nums)

        n = p = length - 1
        while True:
            if n >= 1 and nums[n] > nums[n - 1]:
                i = n - 1
                break
            elif n >= 1:
                n -= 1
            else:
                break
        if i == -1:
            nums.sort()
            # print(nums)
            return
        while True:
            if p >= 1 and nums[p] > nums[i]:
                break
            elif p >= 1:
                p -= 1
            else:
                break
        nums[i], nums[p] = nums[p], nums[i]
        # nums.sort()
        # 需要排序nums[i]之后的所有元素
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


        print(nums)


so = Solution()
so.nextPermutation([1,3,2])
# nn = [1, 3, 2]
# nn1 = nn[1:]
# nn1.sort()
# print(f"{nn1=}")
# nn.sort()
# print(f"{nn=}")
