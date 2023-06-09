# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/10 18:06
 Tool   : PyCharm
 Content: 加1
 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res_lst = []
        s_lst = [str(digit) for digit in digits]
        s = ''
        for i in range(len(digits)):
            s += s_lst[i]
        print(s)
        int_num = int(s)
        print(f"{int_num=}")
        result = int_num + 1
        s_result = str(result)
        for s in range(len(s_result)):
            res_lst.append(int(s_result[s]))
        # int_lst = [int(s) for s in s_lst]
        # result = int_lst + 1
        # ss_lst = str(result)
        # res_lst = [int(x) for x in ss_lst.split()]
        return res_lst

so = Solution()
r_lst = so.plusOne([1,2,3])
print(f"{r_lst=}")


