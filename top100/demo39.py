# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/2 12:16
 Tool   : PyCharm
 Content: 组合总和
 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个
"""
from typing import List


class Solution:
    # 传统深度优先解法
    # 增加begin作为for循环的起始值，用于剪枝，前面使用过的元素，后面的分支不再使用，去除重复解
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # 定义深度优先算法的实现
        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            # 从剩下的元素中，依次取出元素与target进行比较，求出下一个target或者终止这条线
            for index in range(begin, size):
                # residue是下一个target
                residue = target - candidates[index]
                # 如果下一个target小于0，则表示这条路径没有符合条件的解，直接终止
                if residue < 0:
                    return
                # target > 0,继续往下找
                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        # 获取传入的数组的长度
        size = len(candidates)
        # 设置后续迭代的开始元素的下标
        begin = 0
        if size == 0:
            return []
        candidates.sort()
        path = []
        res = []
        dfs(candidates, begin, size, path, res, target)

        return res


so = Solution()
res_path = so.combinationSum([10,1,2,7,6,1,5], 8)
print(f"{res_path=}")
