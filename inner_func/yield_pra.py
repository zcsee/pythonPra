#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fab(max_n):
    nn, a, b = 0, 0, 1
    while nn < max_n:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        nn = nn + 1


for n in fab(5):
    print(n)
print("哈哈哈哈")

# 一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，直到对其调用 next()
# （在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
# 看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
# yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
# 如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
