# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/24 9:33
 Tool   : PyCharm
 Content: 
"""




def main():
    x = 121
    # 两边向中间靠拢
    # x_str = str(x)
    # length = len(x_str) - 1
    # init = 0
    # while length != init:
    #     if x_str[init] == x_str[length]:
    #         init +=1
    #         length -= 1
    #     else:
    #         return False
    # return True
    # 翻转后比较
    x_str = str(x)
    x_str_lsts = list(x_str)
    x_str_reverse_lst = list(x_str)
    x_str_reverse_lst.reverse()
    print(x_str_reverse_lst)
    if x_str_lsts == x_str_reverse_lst:
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    main()
