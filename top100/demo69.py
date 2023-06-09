# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/11 10:48
 Tool   : PyCharm
 Content: x的平方根
 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5
"""

# 解法1
# 袖珍计算器算法」是一种用指数函数 \expexp 和对数函数 \lnln 代替平方根函数的方法
import math


class Solution:
    # 袖珍计算机法
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    # 二分查找法
    def mySqrt2(self, x: int) -> int:
        if x == 0:
            return 0
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    # 牛顿迭代法
    def mySqrt3(self, x: int) -> int:
        if x == 0:
            return 0

        C, x0 = float(x), float(x)
        while True:
            xi = 0.5 * (x0 + C / x0)
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


so = Solution()
an = so.mySqrt2(17)
print(f"{an=}")
