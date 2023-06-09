# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/12 16:45
 Tool   : PyCharm
 Content: 课程表
 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false
"""
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        # 记录入度
        indeg = [0] * numCourses

        for info in prerequisites:
            # 记录有向边
            edges[info[1]].append(info[0])
            # 计算该点对应的入度
            indeg[info[0]] += 1

        # 将当前入度为0的放到双端队列里去
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        # 设置visited变量，记录入度为0的点数
        visited = 0
        result = list()
        # 当双端队列中有入度为0的点时，进行处理
        while q:
            # 记录入度为0的数量
            visited += 1
            # 将入度为0的点弹出
            u = q.popleft()
            # 加入到结果中
            result.append(u)

            # 更新有向边中的以u为起点的点的入度，全部减1
            for v in edges[u]:
                indeg[v] -= 1
                # 如果减掉以u为起点的入度后，入度为0，则将该点加入到入度为0的队列中
                if indeg[v] == 0:
                    q.append(v)
        # 返回入度为0的点数和总点数的比较结果
        # return visited == numCourses
        return result


so = Solution()
res_bool = so.canFinish(3, [[1, 0], [2, 1], [2, 0]])
print(f"{res_bool=}")
