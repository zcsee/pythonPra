# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/12 11:11
 Tool   : PyCharm
 Content: 
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            # 判断指定的网络中元素是否等于word中的第k个元素，不等则此路不通
            if board[i][j] != word[k]:
                return False
            # 如果匹配完整个字符串，则返回True
            if k == len(word) - 1:
                return True
            # 记录当前的访问坐标
            visited.add((i, j))
            # 预设结果为False
            result = False

            # 具体查找下一个字符的步骤，上下左右
            for di, dj in directions:
                newi, newj = i + di, j + dj
                # 判断下标的合法性
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    # 如果该元素未被访问过，则进行递归查找
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


so = Solution()
res_bool = so.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
print(f"{res_bool=}")
