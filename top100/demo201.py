# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/10 14:10
 Tool   : PyCharm
 Content: 数字范围按位与
 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）
"""
from functools import reduce


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # for测试使用
        ans = reduce(lambda x,y:x^y,[x for x in range(left,right+1)])
        print(f"{ans=}")

so = Solution()
res = so.rangeBitwiseAnd(5,7)
print(f"{res=}")

