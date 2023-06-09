def foo():
    print("starting...")
    for i in range(4):
        res = yield 4
        print("res:", res)

    # 当我们添加新的yield
    for i in range(6):
        res = yield 5
        print("res", res)


# 此时未打印出任何信息，说明只是生成了generator对象，并未执行函数
g = foo()

# 在一个def中，如果有多个yiled，在外面通过next迭代生成器时，需要执行两个yield加起来的次数，才能迭代完
for i in range(8):
    print(next(g))
