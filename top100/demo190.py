# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/8/8 11:46
 Tool   : PyCharm
 Content: 颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
输入：n = 00000010100101000001111010011100
输出：964176192 (00111001011110000010100101000000)
解释：输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
            print(f"{i=}")
            print(f"{res=:0b}")
            print(f"{n=:0b}")

        return res


so = Solution()
ans = so.reverseBits(0b00000010100101000001111010011100)
print(f"{ans=}")
