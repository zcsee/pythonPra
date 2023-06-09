# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 13:00
 Tool   : PyCharm
 Content: 给你一个整数，将其转为罗马数字
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        # 枚举
        roman_table = [('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
                       ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
                       ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
                       ('', 'M', 'MM', 'MMM')]
        tmp = num
        n = 0
        res_lst = []
        res_str = ''
        while tmp:
            nu = tmp % 10
            tmp //= 10
            res_lst.insert(0,(n,nu))
            n += 1
            # print(res_lst)
        for ind, nn in res_lst:
            res_str += roman_table[ind][nn]
        # print(res_str)
        return res_str


def main():
    so = Solution()
    so.intToRoman(215)


if __name__ == '__main__':
    main()
