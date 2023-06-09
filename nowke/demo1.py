# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 18:42
 Tool   : PyCharm
 Content: 蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
            例如，当输入5时，应该输出的三角形为：
            1 3 6 10 15
            2 5 9 14
            4 8 13
            7 12
            11
"""


class Solotion():
    def snakes(self, row: int):
        # if row == 1: print(1)
        num = 1
        res_lst = []
        n = row -1
        for _ in range(row):
            res_lst.append([])

        for i in range(row):
            for j in range(i+1):
                """
                如果下标为 i - j，则优先选行
                    1 3 6 
                    2 5 
                    4 
                """
                res_lst[i - j].append(num)
                '''
                如果下标为 j，则优先选列
                    1 2 4
                    3 5
                    6
                '''
                # res_lst[j].append(num)
                num += 1
        # print(res_lst)
        # while res_lst:
        #     print(res_lst.pop())
        for i in range(row):
            for j in range(len(res_lst[i])):
                print(f'{res_lst[i][j]:4d}',end='')
            print('')


so = Solotion()
so.snakes(1)