def by_line_read(filename):
    with open(filename) as f:  # 打开文件
        line = f.readline()  # 读取一行内容
        print('----1----')
        while line:
            print('-----2----')
            yield line
            line = f.readline()  # 不断循环读取
            print('----3-----')


if __name__ == '__main__':
    # read是一个生成器对象
    read = by_line_read(r'D:\python\leetcode\yield_pra\yield_read_file.txt')
    print(read)

    # 读取test两行内容
    for i in range(3):
        print(next(read))
    # print(next(read))

