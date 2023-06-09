# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/5/18 10:51
 Tool   : PyCharm
 内容    : 编写装饰器并装配到指定函数上
 作用    : 在不改变指定函数内容以及函数调用方式的情况下，通过装配装饰器的方式，增加函数的功能
"""
import functools
import time

username, password = "jason", "jason"


# 带参数的装饰器，通过参数控制被装饰的函数的执行次数，并最终返回被装饰函数的返回值
def repeat(_func=None, *, number_times=2):
    def do_twice(func):
        @functools.wraps(func)
        def wrapper_do_twice(*args, **kwargs):
            for _ in range(number_times):
                star_time = time.time()
                res = func(*args, **kwargs)
                stop_time = time.time()
                print(f"运行时间为:{stop_time - star_time}")
            return res
        return wrapper_do_twice
    return do_twice


def auth(func):
    def wrapper(*args, **kwargs):
        user = input("input username pls: ")
        passwd = input("input password pls: ")

        if user == username and passwd == password:
            print("Auth success.")
            func(*args, **kwargs)
        else:
            print("Auth failed.")

    return wrapper


def test(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print(f"运行时间为{stop_time - start_time}")

    return deco


@auth
def bar(name):
    time.sleep(2)
    print(name)
    print("in the bar.")


@repeat(number_times=2)
def foo(name):
    print(f"In the foo.{name}")
    print(foo)
    time.sleep(2)
    return "I am foo."


def main():
    bar("jason")
    # print(foo("alex"))


if __name__ == "__main__":
    main()
