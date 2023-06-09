# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/26 21:09
 Tool   : PyCharm
 Content: 
"""
import math
from typing import List


class Solution:
    def threeSumClosest(sself, nums: List[int], target: int) -> int:
        nums.sort()

        length = len(nums)
        inx_r = length - 1

        res_lst = set()

        for inx in range(length - 2):
            # if nums[inx] > 0:
            #     break
            # if inx > 0 and nums[inx] == nums[inx - 1]:
            #     continue
            inx_l = inx + 1
            inx_r = length - 1
            Flag = False
            while inx_l < inx_r:
                sum = nums[inx] + nums[inx_l] + nums[inx_r]

                # if sum == 0:
                #     res_lst.append([nums[inx], nums[inx_l], nums[inx_r]])
                res_lst.add(sum)
                if Flag:
                    #     # 当三数之和小于0，左指针右移
                    inx_l += 1
                    # Flag = False
                # while inx_l < inx_r and  nums[inx_l] == nums[inx_l-1]:
                #     inx_l += 1
                else:
                    #     # 否则右指针左移
                    inx_r -= 1
                    # Flag =True
                # while inx_l < inx_r and  nums[inx_r] == nums[inx_r + 1]:
                #     inx_r -= 1
            inx_l = inx + 1
            inx_r = length - 1
            Flag = True
            while inx_l < inx_r:
                sum = nums[inx] + nums[inx_l] + nums[inx_r]
                res_lst.add(sum)
                if Flag:
                    inx_l += 1
                else:
                    inx_r -= 1
        res = 0
        min_t = math.pow(2, 31) - 1
        for item in res_lst:
            print(f'{item=},{item-target=}')
            if abs(tmp := item - target) < abs(min_t):
                res = item
                min_t = tmp
                print(f'{tmp=},{min_t=},{item=}')
        # print(res)
        return res

    def threeSumClosest2(sself, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        res = math.pow(2, 31) - 1
        for inx in range(length - 2):
            inx_l = inx + 1
            inx_r = length - 1

            while inx_l < inx_r:
                sum = nums[inx] + nums[inx_l] + nums[inx_r]
                tmp = sum - target

                if abs(tmp) < abs(res):
                    res = sum
                if sum - target < 0:
                    inx_l += 1
                elif sum == target:
                    return sum
                else:
                    inx_r -= 1
        return res


so = Solution()
result = so.threeSumClosest2([1, 2, 4, 8, 16, 32, 64, 128], 82)
print(result)
