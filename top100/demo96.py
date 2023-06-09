# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/15 14:45
 Tool   : PyCharm
 Content: 不同的二叉搜索树
 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # 
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]
