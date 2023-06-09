# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/22 10:48
 Tool   : PyCharm
 Content: 
"""


def get_sum(a, b):
    return a + b


def main():
    lst_1 = [1, 2, 3, 4, 5]
    lst_2 = [1, 2, 3, 4, 5]

    lst_3 = list(map(lambda a, b: a + b, lst_1, lst_2))
    lst_4 = list(map(get_sum, lst_1, lst_2))

    print(f'{lst_3=}')
    print(f'{lst_4=}')
    pass


if __name__ == '__main__':
    main()
