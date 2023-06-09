# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/22 14:59
 Tool   : PyCharm
 Content: 
"""


def main():
    s = "dvdf"

    n = len(s)
    if n == 0:
        return 0

    a = s[0]
    result = 1

    for i in range(1,len(s)):
        if s[i] in a:
            result = max(result, len(a))
            # 通过str的find方法，获取到当前子字符串的索引
            inx = s.find(s[i])
            a = a[inx+1:] + s[i]
        else:
            a += s[i]
    # print(len(a))
    print(max(len(a), result))


if __name__ == "__main__":
    main()
