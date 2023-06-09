# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/6 15:41
 Tool   : PyCharm
 Content: 
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1

        # 判断x是否为0
        if x == 0.0:
            return 0.0

        # 如果幂次小于0，则将其修复为正的
        if n < 0:
            x, n = 1 / x, -n

        # 如果n不为0
        while n:
            print(f"{n=}")
            # 如果n为奇数，先乘一次
            if n & 1:
                ans *= x

            # 如果n为偶数，基数自己做一次平方操作，可以减少操作的次数
            x *= x

            # n除以2
            n >>= 1

        return ans


so = Solution()
ans = so.myPow(5, 9)
print(ans)
