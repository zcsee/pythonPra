# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/28 11:42
 Tool   : PyCharm
 Content: 
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n-2):
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] - target  >  -nums[p] - nums[q]:
                        q -= 1
                    elif nums[i] + nums[k] -target  < -nums[p] - nums[q]:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        # 左指针一直移动到当前重复元素的最右边
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        # 右指针一直移动到当前重复元素的最左边
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        # 找到符合条件的组合后，左右指针都往中间收缩
                        p += 1
                        q -= 1
        return res


so = Solution()
res = so.fourSum([1,0,-1,0,-2,2],0)
print(f'{res=}')