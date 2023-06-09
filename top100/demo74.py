# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/11 15:21
 Tool   : PyCharm
 Content: 搜索二维矩阵
 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数
"""
from typing import List


class Solution:
    # 将二维矩阵视为一个列表来进行二分查找
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) >> 1
            x, y = mid // n, mid % n
            if matrix[x][y] > target:
                r = mid - 1
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                return True
        return False


so = Solution()
result_bool = so.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
print(f"{result_bool=}")
