# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/7/2 17:05
 Tool   : PyCharm
 Content: 
"""


class Solution():
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1_l = list(num1)
        num1_l = [int(i) for i in num1_l]
        num2_l = list(num2)
        num2_l = [int(i) for i in num2_l]
        result = [0] * (len(num1) + len(num2))
        # print(f"{num1_l=}")
        # print(f"{num2_l=}")
        # print(f"{result=}")

        # 逆序遍历，但是index还是从左到右的
        for i in range(len(num1_l) - 1, -1, -1):  # 被乘数
            # print(f"{i=}")
            for j in range(len(num2_l) - 1, -1, -1):  # 乘数
                # print(f"{j=}")
                temp = num1_l[i] * num2_l[j]

                # 个位
                idx = i + j + 1
                # 十位
                idx2 = i + j

                # 先相加，再进位
                temp += result[idx]
                result[idx] = temp % 10  # 个位直接取余
                # 十位要加到现有十位上，小于10的时候，除法结果是0
                result[idx2] += temp // 10

        # print(result)
        if result[0] == 0:
            result = result[1:]
        re_str = "".join(str(i) for i in result)
        return re_str


so = Solution()
str_re = so.multiply('123','456')
print(f"{str_re=}")

test_nums = [1, 2, 3, 4]
# range(3, -1, -1)
for i in range(len(test_nums) -1 ,-1 , -1):
    print(test_nums[i],end=' ')
# 输出
# 4 3 2 1