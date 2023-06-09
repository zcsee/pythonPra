# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/23 23:57
 Tool   : PyCharm
 Content: 
"""

import math


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            x = -x
            flag = False
        while x != 0:
            tmp = x % 10
            if result > 214748364 or (result == 214748364 and tmp > 7):
                return 0
            if -result < -214748364 or (-result == -214748364 and tmp < -8):
                return 0

            result = result * 10 + tmp
            x //= 10
        if flag:
            return result
        else:
            return -result


def main():
    so = Solution()
    xx = so.reverse(int(-123))
    print(xx)
    # print(math.pow(2, 31))
    pass


if __name__ == '__main__':
    main()
