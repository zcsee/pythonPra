# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/30 17:07
 Tool   : PyCharm
 Content: 搜索旋转排序数组
 整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 如果输入的是一个空列表，返回-1
        if not nums:
            return -1
        length_nums = len(nums)
        l, r = 0, length_nums - 1

        while l <= r:
            mid = (l + r) // 2
            # 如果中点为目标值，返回中点的下标
            if nums[mid] == target:
                return mid
            # 如果中点大于等于起始元素，则左半为有序数组，进行二分查找
            if nums[l] <= nums[mid]:
                # 如果目标值在其中，则右边界移动到原来的中点的左边，抛弃掉右半边
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                    # 否则，左边界移动到中点的右边，抛弃到整个列表的左半边
                else:
                    l = mid + 1
            # 如果左半非有序，则右边有序，进行二分查找
            else:
                if nums[mid] < target <= nums[length_nums - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


so = Solution()
res = so.search([3, 4, 5, 0, 1, 2], 0)
print(res)
