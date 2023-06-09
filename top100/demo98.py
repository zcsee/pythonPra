# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/16 15:54
 Tool   : PyCharm
 Content: 验证二叉搜索树
 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 用递归的方式，验证每个子树是否符合二叉搜索树的规则，
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower=float('-inf'), upper=float('inf')) -> bool:
            # 如果传入的节点的为空，则直接返回True，继续其他判断
            if not node:
                return True
            # 判断的值为传入的节点值
            val = node.val

            # 如果当前的值小于等于左边界，或者大于等于右边界，则不符合二叉搜索树，返回False
            if val <= lower or val >= upper:
                return False

            # 搜索右子树
            if not helper(node.right, val, upper):
                return False
            # 搜索左子树
            if not helper(node.left, lower, val):
                return False
            # 如果未发现不符合的情况，则返回True
            return True

        return helper(root)

    # 使用中序遍历的方式来进行二叉搜索树的验证
    def isValidBST2(self, root: TreeNode) -> bool:
        # 定义一个栈，用于临时存放未使用的做节点
        stack, inorder = [], float('-inf')

        # 如果栈里有元素或root不为空，则说明还没有遍历完
        while stack or root:
            # 如果root不为None，说明还有左节点
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            # 如果中序遍历得到的节点的值小于前一个inorder，则说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
