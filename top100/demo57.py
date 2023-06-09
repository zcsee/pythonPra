# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 16:06
 Tool   : PyCharm
 Content: 插入区间
 给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans_lst = []

        # 先将数组直接合并
        intervals.append(newInterval)
        # 必须排序
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if not ans_lst or ans_lst[-1][1] < interval[0]:
                ans_lst.append(interval)
            else:
                ans_lst[-1][1] = max(ans_lst[-1][1], interval[1])
        return ans_lst

so = Solution()
res_lst = so.insert(intervals = [[1,3],[6,9]], newInterval = [2,5])
print(f"{res_lst=}")