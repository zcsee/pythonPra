# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/1 16:47
 Tool   : PyCharm
 Content: 外观数组
"""


class Solution:
    # 方法1：逐次生成外观数组，达到指定次数后输出
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for i in range(n - 1):
            curr = ""
            pos = 0
            start = 0

            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr

        return prev
    # 方法2：n的最大值为30，可以预先打表，然后搜索
    


so = Solution()
res_str = so.countAndSay(5)
print(res_str)