import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array(4)

c = a - b
print c

c = a + b
print c

c = a * b
print c

c = b ** 2
print c

c = 10*np.sin(a)
print c

print b < 3

a = np.array([[1, 1], [0, 1]])
b = np.arange(4).reshape((2, 2))

print a
print b

c = a * b
print c
c_dot = np.dot(a, b)
print c_dot

a = np.random.random((2, 4))
print a

print np.sum(a)
print np.min(a)
print np.max(a)

a = np.arange(2, 14).reshape((3, 4))
print np.argmin(a)
print np.argmax(a)
print np.mean(a)
print np.average(a)
print np.cumsum(a)
print np.diff(a)
print np.nonzero(a)

a = np.arange(14, 2, -1).reshape((3, 4))
print np.sort(a)
print a.T
print np.clip(a, 5, 9)
