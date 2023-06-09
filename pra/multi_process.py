from multiprocessing import Process
import multiprocessing
import os
import time


def task_process(delay):
    num = 0
    for i in range(delay * 100000000):
        num += 1
    print(f"进程pid为{os.getpid()},执行完成。")


if __name__ == '__main__':
    print('父进程pid为 %s.' % os.getpid())
    t0 = time.time()
    task_process(1)
    task_process(1)
    t1 = time.time()
    print(f"顺序执行耗时 {t1 - t0}")
    p0 = Process(target=task_process, args=(1,))
    p1 = Process(target=task_process, args=(1,))
    # p0.daemon = True
    t2 = time.time()
    p0.start()
    p1.start()
    print(f"p0的激活状态:{p0.is_alive()}")
    # p0.join()
    # p1.join()
    t3 = time.time()
    print(f"多进程执行耗时 {t3 - t2}")

    pipe = multiprocessing.Pipe()
