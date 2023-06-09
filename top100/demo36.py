# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/1 15:28
 Tool   : PyCharm
 Content: 数独的有效性
 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
"""
from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        set_vaild = set()
        # 判断行
        for item in board:
            valid_count = 0
            set_vaild.clear()
            for i in item:
                if i != '.':
                    set_vaild.add(i)
                    valid_count += 1
            if num := len(set_vaild) != valid_count:
                return False
        # 判断列
        for i in range(9):
            valid_count = 0
            set_vaild.clear()
            for j in range(9):
                if board[j][i] != '.':
                    set_vaild.add(board[j][i])
                    valid_count += 1
            if num := len(set_vaild) != valid_count:
                return False
        # 判断九宫格
        for ge in range(1,4):
            for i in range(ge * 3):
                valid_count = 0
                set_vaild.clear()
                for j in range(ge * 3):
                    print(f"{ge=},{i=},{j=}")
                    if board[j][i] != '.':
                        set_vaild.add(board[j][i])
                        valid_count += 1
                print(set_vaild)
            if num := len(set_vaild) != valid_count:
                return False

    def isValidSudokus2(self, board: List[List[str]]) -> bool:
        # 0: row, 1: column, 2: square
        record = {0: defaultdict(set), 1: defaultdict(set), 2: defaultdict(set)}
        n = len(board)
        m = sqrt(n)
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in record[0][i] or board[i][j] in record[1][j]:
                    return False
                sq = i // m * m + j // m
                if board[i][j] in record[2][sq]:
                    return False
                record[0][i].add(board[i][j])
                record[1][j].add(board[i][j])
                record[2][sq].add(board[i][j])
        return True


so = Solution()
res_bool = so.isValidSudokus2([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])

print(f"{res_bool=}")
