# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/15 14:13
 Tool   : PyCharm
 Content: 不同的二叉搜索树II
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def gs(start, end):
            if start > end:
                # 如果返回的是个空列表，会报错，因为空列表不能迭代
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = gs(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = gs(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return gs(1, n) if n else []

so = Solution()
res = so.generateTrees(8)
print(f"{res=},{len(res)=}")
