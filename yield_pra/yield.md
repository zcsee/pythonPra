yield的用途
1、将函数改造成一个迭代器的模式
`def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1
 
for n in fab(5): 
    print n`
2、用于文件读取时，利用固定长度的缓冲区来不断读取文件，避免不可预测的内存占用
`def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return`