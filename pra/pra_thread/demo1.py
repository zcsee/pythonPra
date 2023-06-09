# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/21 15:38
 Tool   : PyCharm
 Content: 
"""
import time
from threading import Thread


class Demo1(Thread):
    def __init__(self, name, count=0):
        super(Demo1, self).__init__(name=name)
        self.count = count

    def run(self) -> None:
        for _ in range(10):
            time.sleep(0.5)
            self.count += 1
            print(f"{self.getName()} -- {self.count}")


def main():
    threads = []
    t1 = Demo1('t1')
    t2 = Demo1('t2')
    threads.append(t1)
    threads.append(t2)

    for thread in threads:
        thread.start()

    # for thread in threads:
    #     thread.join()

    print(f"finished {threads}")


if __name__ == "__main__":
    main()
