# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 14:16
 Tool   : PyCharm
 Content: 螺旋矩阵
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans_lst = []
        m = len(matrix)
        n = len(matrix[0])
        # 获取四个边界
        top, bottom, left, right = 0, m - 1, 0, n - 1

        if matrix is None:
            return ans_lst

        while True:
            # 上
            for i in range(left, right + 1):
                ans_lst.append(matrix[top][i])
            top += 1

            if top > bottom:
                break
            # 右
            for i in range(top, bottom + 1):
                ans_lst.append(matrix[i][right])
            right -= 1

            if right < left:
                break

            # 下
            for i in range(right, left - 1, -1):
                ans_lst.append(matrix[bottom][i])
            bottom -= 1

            if bottom < top:
                break
            # 左
            for i in range(bottom, top - 1, -1):
                ans_lst.append(matrix[i][left])
            left += 1

            if left > right:
                break

        return ans_lst


so = Solution()
res_lst = so.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# res_lst = so.spiralOrder()
print(f"{res_lst=}")
