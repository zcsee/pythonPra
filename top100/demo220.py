# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/18 10:15
 Tool   : PyCharm
 Content: 
"""
import bisect
from typing import List

from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True
        return False


so = Solution()
res_bool = so.containsNearbyAlmostDuplicate(nums=[1, 2, 3, 1], k=3, t=0)
print(f"{res_bool=}")
