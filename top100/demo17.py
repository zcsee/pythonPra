# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/27 21:48
 Tool   : PyCharm
 Content: 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['q', 'p', 'r', 's'], '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []

        # 回溯
        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                combination_lst.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])

        combination_lst = []
        backtrack('', digits)
        return combination_lst

    # 队列
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # 用列表来加上pop(0)来模拟先进先出队列
        queue = ['']
        for digit in digits:
            for _ in range(len(queue)):
                # 将原先队列中的第一个元素弹出
                tmp = queue.pop(0)
                # 分别加上后面字母列表中的每个字符后，重新入队
                for letter in phone[ord(digit) - 50]:  # 这里我们不使用 int() 转换字符串，使用ASCII码 ord('2')=50
                    queue.append(tmp + letter)
        return queue


dig = '0'
print(f'{ord(dig)=},{ord(dig)-50=}')

# so = Solution()
# res = so.letterCombinations2('23')
# print(res)
