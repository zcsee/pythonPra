# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/19 23:05
 Tool  : PyCharm
"""

dic_color = {'pink': "p", 'green': "g"}


def main():
    print(dic_color.pop(input("输入你要知道的颜色简写:"), None) or "hello")
    pass


if __name__ == "__main__":
    main()