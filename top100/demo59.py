# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/7 16:29
 Tool   : PyCharm
 Content: 螺旋矩阵II
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top, right, bottom, left = 0, n - 1, n - 1, 0
        num = 1
        nn = n * n
        while True:

            # 上
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
                # print(f"top{num=}")
                # print(f"{matrix=}")
            top += 1
            if num > nn:
                break
            # 右
            for i in range(top, bottom):
                matrix[i][right] = num
                num += 1
                # print(f"right{num=}")
                # print(f"{matrix=}")
            right -= 1
            if num > nn:
                break
            # 下
            for i in range(right + 1, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
                # print(f"bottom{num=}")
                # print(f"{matrix=}")
            bottom -= 1
            if num > nn:
                break
            # 左
            for i in range(bottom, top-1, -1):
                matrix[i][left] = num
                num += 1
                # print(f"left{num=}")
                # print(f"{matrix=}")
            left += 1
            if num > nn:
                break

            # print(num)
        # print(f"{matrix=}")
        return matrix


so = Solution()
res_lst = so.generateMatrix(7)
print(f"{res_lst=}")
