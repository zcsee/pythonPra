# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 0:34
 Tool   : PyCharm
 Content: 
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        nums = [str(x) for x in range(10)]
        flag = True
        stop = False
        result = 0
        xx = False
        for c in s:
            if c == ' ' and stop is False and xx is False:
                continue
            if c == ' ' and stop:
                break
            if c == ' ' and stop is False:
                if xx:
                    return 0
            if c == '-' and stop is False:
                flag = False
                if xx:
                    return 0
                else:
                    xx = True
            if c.isalpha() and stop is False:
                return 0
            if c.isalpha() and stop is True:
                break
            if c == '.' and stop is False:
                return 0
            if c == '.' and stop is True:
                break
            if c == '+' and stop is False:
                if xx:
                    return 0
                else:
                    xx = True
            if c == '+' and stop:
                break
            if c == '-' and stop:
                break
            if c in nums:
                stop = True
                result = result * 10 + int(c)
                if flag:
                    if result > 2147483647:
                        return 2147483647
                else:
                    if -result < -2147483648:
                        return -2147483648
            # print(c)
        if flag:
            return result
        else:
            return -result

    def myAtoi2(self, s: str) -> int:
        import re
        result = 0
        match_patern = '[ ]*([+-]?\d+)'
        mat = re.match(match_patern, s)
        if mat:
            result = mat.group(1)
            if -2147483648 <= result <= 2147483647:
                return result
            else:
                return 0

        return result



so = Solution()
res = so.myAtoi('  ddd -123')
print(res)
