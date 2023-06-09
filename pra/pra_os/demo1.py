# -*- coding: utf-8 -*-
"""
 Author: Jason See
 Date  : 2022/5/24 11:34
 Tool  : PyCharm
 lib   : os 库
 Content: 系统相关变量和操作
"""
import os

# 系统相关变量
# 获取操作系统类型
import time

print(os.name)
# 获取环境变量
# print(os.environ)
# 获取系统路径分割符
print(os.sep)
# 获取路径变量的分割符
print(os.pathsep)
# 获取换行分隔符, /r/n 被执行了，待研究打印方法
# TODO
print(os.linesep)

# 文件目录操作
# os.mkdir("stdos")
# 当exist_ok为False时，会检测目录是否存在，存在则不执行，不报错
os.makedirs(name="stdos", exist_ok=True)
# 当exist_ok为False时，会检测目录是否存在，存在则报错
# os.makedirs(name="stdos", exist_ok=False)
# os.rmdir("stdos")
# 获取当前所在路径
print(os.getcwd())

# os.path
base_path = os.getcwd()
abs_path = base_path + "\\" + "demo1.py"
file = "demo1.py"
# 获取指定文件的绝对路径
print(os.path.abspath("demo1.py"))
# 判断传入的变量是不是一个绝对路径
print(os.path.isabs(abs_path))
# 将绝对路径进行分割为基础路径和文件名,返回一个元组，包含基础路径和文件名两个元素
print(os.path.split(abs_path))

# 判断文件是否存在
print(os.path.exists(file))
# 获取文件的最后更改时间，返回值为一个时间戳
atime = os.path.getatime(file)
print(atime)
# 通过time.localtime()获取时间戳对应的时间，返回一个time.struct_time对象
local_time = time.localtime(atime)
print(type(local_time))
print(local_time)
# 通过time.strftime方法将time.struct_time对象进行格式化
str_time = time.strftime("%Y-%m-%m %H:%M:%S", local_time)
print(str_time)

# 获取文件的创建时间
print(os.path.getctime(file))
print(f"文件的创建时间为{time.strftime('%Y-%m-%m %H:%M:%S', time.localtime(os.path.getctime(file)))}")

# 获取的文件的大小，单位为字节
print(f"文件的大小为{os.path.getsize(file)}字节")

# 创建测试文件，用于测试删除功能,windows上执行失败，在linux上执行成功
# os.mknod("test_mknod.txt")
# 通过open进行创建空文件,在windows上创建成功
open("open_test_empty_file.txt", "a").close()
# 文件删除
os.remove("open_test_empty_file.txt")


# 执行命令和管理进程
# 使用python的os库来执行命令，不推荐，已有其他库支持
# os.system
os.system("python hello_world.py")
# 通过windows命令 chcp 65001能解决部分问题，仍存在中文乱码的问题
os.system("chcp 65001")
print(os.system("ipconfig"))

# os.popen
p_res = os.popen("ipconfig")
# 与os.system的执行命令想通过，但结果无乱码
print(p_res.read())