# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/22 16:03
 Tool   : PyCharm
 Content: 
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        nums3.extend(nums1)
        nums3.extend(nums2)
        nums3.sort()


        if (length := len(nums3)) % 2:
            print(f"{length=}")
            print(nums3)
            mid = length//2
            print(f"{mid}")
            print(f"{nums3[mid]=}")
        else:
            print((nums3[length//2] + nums3[length // 2 + 1]) / 2.0)


def main():
    so = Solution()
    so.findMedianSortedArrays([1, 3, 5, 7,9], [2, 4, 6, 8])


if __name__ == '__main__':
    main()
