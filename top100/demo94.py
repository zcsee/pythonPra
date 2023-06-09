# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/15 13:48
 Tool   : PyCharm
 Content: 二叉树的中序遍历
 给定一个二叉树的根节点 root ，返回 它的 中序 遍历
"""

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归的方法
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root)
            dfs(root.right)

        dfs(root)
        return res

    # 迭代的方法
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """
        		:type root: TreeNode
        		:rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res


so = Solution()
res = so.inorderTraversal()
print(f"{res=}")
