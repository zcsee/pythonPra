from multiprocessing import Process, Queue
import time


def product(q):
    count = 1
    while True:
        q.put(f"冷饮 {count}")
        print(f"{time.strftime('%H:%M:%S')} A放入：[冷饮：{count}]")
        count += 1
        time.sleep(1)


def consumer(q):
    while True:
        print(f"{time.strftime('%H:%M:%S')} B取出：[冷饮：{q.getMessage()}]")
        time.sleep(5)


if __name__ == '__main__':
    q = Queue(maxsize=5)
    p = Process(target=product, args=(q,))
    c = Process(target=consumer, args=(q,))
    c.start()
    p.start()
    c.join()
    p.join()
