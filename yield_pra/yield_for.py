#!/usr/bin/python
# -*- coding: UTF-8 -*-
# function: 测试yield和return的实现方式异同点

print('yield:')


def _testyield():
    for i in range(5):
        yield i * i


# 这里产生生成器对象,跟java对象意思相同
generator = _testyield()

for i in range(5):
    print(next(generator))

# -----------------------------------------------------------#

print('return:')


def _return(n):
    # 这里res是一个list[],得出的结果是[1,2,3,4,5]
    res = [i * i for i in range(n)]
    return res


for i in _return(5):
    print(i)
