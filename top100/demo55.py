# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 14:44
 Tool   : PyCharm
 Content: 跳跃游戏
 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res_bool = False
        n = len(nums)
        if not nums:
            return res_bool
        max_pos = 0
        for i in range(n):
            # 判断能达到的区间的元素
            if i <= max_pos:
                max_pos = max(i + nums[i], max_pos)
                if max_pos >= n - 1:
                    return True
        return res_bool


so = Solution()
result_bool = so.canJump([3, 2, 1, 0, 4])
print(f"{result_bool=}")
