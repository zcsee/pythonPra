# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/9 21:35
 Tool   : PyCharm
 Content: 不同路径2
 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        # 计算网格的行数和列数
        # 行数
        m = len(obstacleGrid)
        # 列数
        n = len(obstacleGrid[0])

        # 计算结果的数组
        d = [[0] * n for _ in range(m)]
        # print(d)

        d[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1 or d[i - 1][0] == 0:
                d[i][0] = 0
            else:
                d[i][0] = 1

        for i in range(1, n):
            if obstacleGrid[0][i] == 1 or d[0][i - 1] == 0:
                d[0][i] = 0
            else:
                d[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]
        print(f"{d=}")
        return d[-1][-1]


so = Solution()
res = so.uniquePathsWithObstacles([[0, 0], [1, 0]])
print(f"{res=}")
