# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/12 14:16
 Tool   : PyCharm
 Content: 搜索旋转排序数组II
 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。
你必须尽可能减少整个操作步骤
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)

        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True

            if nums[l] == nums[mid] and nums[r] == nums[mid]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False


so = Solution()
res_bool = so.search(nums=[2, 5, 6, 0, 0, 1, 2], target=1)
print(f"{res_bool=}")
