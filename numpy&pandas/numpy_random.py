import numpy as np


def mean(size, count):
    s = 0.0
    for i in range(count):
        a = np.random.uniform(0, 1, size)
        m = np.max(a)
        s += m
    return s / count


if __name__ == "__main__":
    print mean(4, 100)
    print mean(4, 1000)
    print mean(4, 10000)
