#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/16 16:23
@Author  : Jason
@Site    : 
@File    : demo2.py
@Project : leetcode
@Software: PyCharm
"""


class Solution:
    def minDeletion(self, nums) -> int:
        ans = 0

        length = len(nums)

        for i in range(length - 2):
            if nums[i] == nums[i + 1]:
                ans += 1
                print(f"{i=}")
            else:
                i += 1

        if (length - ans) % 2 == 1:
            ans += 1

        return ans


if __name__ == "__main__":
    sl = Solution()
    result = sl.minDeletion([3, 4, 8])
    print(f"{result=}")
