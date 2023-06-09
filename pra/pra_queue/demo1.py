# -*- coding: utf-8 -*-
"""
 Author : Jason See
 Date   : 2022/6/21 16:17
 Tool   : PyCharm
 Content: 
"""
import threading
import time
from queue import Queue

my_queue = Queue()


def consumer():
    print(f'I am consumer. waiting...')
    my_queue.get()
    print(f"consumer done.\n")


thread = threading.Thread(target=consumer)
thread.start()

time.sleep(2)
print(f'product putting...')
my_queue.put(object())
print(f'product done\n')
thread.join()
