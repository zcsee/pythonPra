# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/2 16:05
 Tool   : PyCharm
 Content: 组合总和II
 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 定义深度优先算法的实现
        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path[:])
                return

            # 从剩下的元素中，依次取出元素与target进行比较，求出下一个target或者终止这条线
            for index in range(begin, len(candidates)):
                # residue是下一个target
                residue = target - candidates[index]
                # 如果下一个target小于0，则表示这条路径没有符合条件的解，直接终止
                if residue < 0:
                    return
                # target > 0,继续往下找
                if index > begin and candidates[index] == candidates[index - 1]:
                    # dfs(candidates[index+1:], index+1, size, path + [candidates[index]], res, residue)
                    continue
                # 因为元素不能重用，所以选择下一个元素
                dfs(candidates, index+1, size, path + [candidates[index]], res, residue)

        # 获取传入的数组的长度
        candidates.sort()
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
res_path = so.combinationSum2([10, 1,1, 2, 7, 6, 1, 5], 8)
print(f"{res_path=}")
