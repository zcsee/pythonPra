#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/16 16:40
@Author  : Jason
@Site    : 
@File    : 1507.py
@Project : leetcode
@Software: PyCharm

给你一个字符date，它的格式为Day Month Year，其中：

Day是集合{"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}中的一个元素。
Month是集合{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}中的一个元素。
Year的范围在 [1900, 2100]之间。
请你将字符串转变为YYYY-MM-DD的格式，其中：

YYYY表示 4 位的年份。
MM表示 2 位的月份。
DD表示 2 位的天数。
"""


class Solution:
    def reformatDate(self, date: str) -> str:
        s2month = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
            "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        date = date.split(" ")

        date[0] = date[0][: -2].zfill(2)
        date[1] = s2month.get(date[1])
        date.reverse()

        return "-".join(date)


if __name__ == "__main__":
    so = Solution()
    result = so.reformatDate('20th Oct 2052')
    print(f"{result=}")
