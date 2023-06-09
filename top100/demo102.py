# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/19 10:16
 Tool   : PyCharm
 Content: 
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        # 使用列表来模拟队列
        queue = [root]

        # 如果队列不为空则进行循环
        while queue:
            # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            size = len(queue)
            tmp = []
            # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
            # 如果节点的左/右子树不为空，也放入队列中
            for _ in range(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            # 将临时list加入最终返回结果中
            res.append(tmp)
        return res


so = Solution()
res_list = so.levelOrder(TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
                                  right=TreeNode(val=3, left=TreeNode(val=6), right=TreeNode(val=7))))
print(f"{res_list=}")
