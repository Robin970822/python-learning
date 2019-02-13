import numpy as np


def record(k):
    diamonds = np.random.uniform(0, 1, 4)
    # print diamonds
    m = np.max(diamonds)
    cur = 0
    value = 0

    if k == 1:
        cur = np.max(diamonds[0])
    else:
        cur = np.max(diamonds[0:k - 1])

    for i in range(4 - k):
        if diamonds[i + k] > cur:
            value = diamonds[i + k]
            return value, m
    return value, m


def exp(k, count):
    cnt = 0.0
    for i in range(count):
        cur, m = record(k)
        if cur == m:
            cnt += 1
    return cnt / count


def distant(v, a):
    s = 0
    for i in range(len(a)):
        s += np.abs(a[i] - v)
    return s


def f(num, count):
    for i in range(count):
        a = np.random.uniform(0, 1, num)
        a = np.cumsum(a)
        print a
        ave = np.mean(a)
        if num / 2 == 1:
            mid = a[num / 2]
        else:
            mid = (a[num / 2] + a[num / 2 - 1]) / 2
        disAve = distant(ave, a)
        disMid = distant(mid, a)
        print ave
        print mid
        print disAve
        print disMid


if __name__ == "__main__":
    f(4, 1)
