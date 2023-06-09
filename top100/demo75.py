# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/11 16:00
 Tool   : PyCharm
 Content: 颜色分类
 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题
"""
from typing import List


class Solution:
    # 暴力破解法
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = nums.count(0), nums.count(1), nums.count(2)
        for i in range(zero):
            nums[i] = 0
        for i in range(zero, zero + one):
            nums[i] = 1
        for i in range(zero + one, zero + one + two):
            nums[i] = 2

    # 双指针一次遍历
    def sortColors2(self, nums: List[int]) -> None:
        p0, p1 = 0, 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1


so = Solution()
so.sortColors2([2, 0, 2, 1, 1, 0])
