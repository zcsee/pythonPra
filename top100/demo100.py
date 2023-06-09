# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/18 16:42
 Tool   : PyCharm
 Content: 
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 如果两者都为空，则返回True
        if not p and not q:
            return True
        # 如果只有一个有空，则返回False
        elif not p or not q:
            return False
        # 如果节点的值不同，则返回False
        elif p.val != q.val:
            return False
        # 如果还有节点没有遍历过，则继续遍历
        else:
            # 先检查左节点，再检查右节点
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


so = Solution()
res_bool = so.isSameTree()
print(f"{res_bool=}")
