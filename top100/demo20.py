# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/28 16:37
 Tool   : PyCharm
 Content: 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
"""

class Solution:
    def isValid(self, s: str) -> bool:
        res_flag = True
        # in_s = '('
        in_s = '('
        out_s = ')'
        in_ss = '['
        out_ss = ']'
        in_sss = '{'
        out_sss = '}'

        s_stack = []
        for c in s:
            if c in in_s:
                s_stack.append(c)
            if c in out_s:
                if s_stack[-1] == in_s:
                    s_stack.pop()
                else:
                    return False
            if c in out_ss:
                if s_stack[-1] == in_ss:
                    s_stack.pop()
                else:
                    return False
            if c in out_sss:
                if s_stack[-1] == in_sss:
                    s_stack.pop()
                else:
                    return False
        if len(s_stack) > 0:
            res_flag = False
        # print(s_stack)
        return res_flag


so = Solution()
res = so.isValid("([)]{}")
print(f'{res=}')