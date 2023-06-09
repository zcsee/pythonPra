# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/23 14:37
 Tool   : PyCharm
 Content: 
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result_lst = []
        result = ''
        if len(s) == 1 or len(s) == 2 or numRows == 1:
            return s

        lst_tmp = []
        for _ in range(numRows):
            lst_tmp.append([])
        zx = [x for x in range(numRows)]
        nx = sorted(zx,reverse=True)
        nx.pop()
        nx.remove(numRows - 1)

        # print(f'{zx=}')
        # print(f'{nx=}')

        # flag为true时，使用正序
        flag = True

        ss = list(s)
        zz = 0
        nnn = numRows-2
        nn = numRows - 1
        while ss:
            if flag:
                lst_tmp[zz].append(ss[0])
                ss.remove(ss[0])
                if zz < nn or zz == 0:
                    zz += 1
                else:
                    zz = 0
                    flag = False
            else:
                if numRows == 2:
                    flag = True
                    continue
                lst_tmp[nnn].append(ss[0])
                ss.remove(ss[0])
                if nnn > 0 and nnn != 1:
                    nnn -= 1
                elif numRows == 2:
                    flag = True
                    nnn = 1
                else:
                    nnn = numRows -2
                    flag = True
        for i in range(len(lst_tmp)):
            for j in range(len(lst_tmp[i])):
                result_lst.append(lst_tmp[i][j])
        for i in range(len(result_lst)):
            result += result_lst[i]
        # print(result)
        # print(result)
        return result

    def convert2(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res_str = ''
        # 构建元素为字符串的数组，长度为numRows的值
        res = ['' for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i ==0 or i == numRows -1:
                flag = -flag
            i += flag
        res_str = ''.join(res)
        return res_str


def main():
    so = Solution()
    # result = so.convert('ABCD', 2)
    # print(result)

    result2 = so.convert2("ABCD", 2)
    print(result2)


if __name__ == '__main__':
    main()
