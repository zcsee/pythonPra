# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/6 15:29
 Tool   : PyCharm
 Content: 
"""
from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_lst = collections.defaultdict(list)

        # 通过遍历将strs中的每个字符串进行排序，进行排序
        for ss in strs:
            s = str(sorted(ss))
            ans_lst[s].append(ss)

        # print(ans_lst.values())
        return ans_lst.values()


so = Solution()
res = so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])