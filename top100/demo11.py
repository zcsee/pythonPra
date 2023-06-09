# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 10:24
 Tool   : PyCharm
 Content: 
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 暴力破解
        height_x = []
        # 构建高度带下标的数组
        for i, x in enumerate(height, 1):
            height_x.append((i, x))
        print(height_x)
        mj_lst = []
        max_s = 0
        while xx := height_x.pop():
            for inx, hh in height_x:
                length = abs(xx[0] - inx)
                hh = min(hh, xx[1])
                s = length * hh
                if s > max_s:
                    max_s = s
                # mj_lst.append(s)
            if len(height_x) == 1:
                break
        # mj_lst.sort()
        print(max_s)
        return max_s
    # 双指针法
    def maxArea2(self, height: List[int]) -> int:
        if len(height) == 2: return min(height[0],height[1])

        left, right = 0, len(height) -1
        max_s = 0
        while right > left:
            s = min(height[left], height[right]) * (right - left)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            if max_s < s:
                max_s = s
        print(max_s)
        return max_s

def main():
    so = Solution()
    # so.maxArea([1, 2, 3, 4, 5, 6, 7, 8])
    so.maxArea2([1,2,3,4,5])


if __name__ == '__main__':
    main()
