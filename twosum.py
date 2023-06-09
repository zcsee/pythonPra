# coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            if num in nums_dict:
                # 如果目标加数出现，则返回已存储的原加数位置和目标加数的位置
                return [nums_dict[num], i]
            else:
                # 如果元素没出现过，则用目标和减去该元素，得到对应的目标加数
                nums_dict[target - num] = i
            print(f"{i=},{num=}")
            print(f"{nums_dict=}")


so = Solution()
print(so.twoSum([4, 0, 0, 2], 6))
