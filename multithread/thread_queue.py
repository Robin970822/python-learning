# coding=utf-8
import threading
import time
from queue import Queue


def job(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)    # 多线程调用的函数不能用return返回值


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3],
            [3, 4, 5],
            [4, 4, 4],
            [5, 5, 5]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    results = []
    for thread in threads:
        thread.join()
        results.append(q.get())
    print results


if __name__ == '__main__':
    multithreading()
