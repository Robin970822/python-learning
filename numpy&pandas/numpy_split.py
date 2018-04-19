import numpy as np

A = np.arange(12).reshape((3, 4))
print A
print np.split(A, 2, axis=1)
print np.split(A, 3, axis=0)

B = np.arange(24).reshape((2, 3, 4))

print np.shape(B)
print B
print np.split(B, 2, axis=0)[0]
print np.split(B, 3, axis=1)[0]
print np.split(B, 2, axis=2)[0]

print np.shape(A)
print A
print np.vsplit(A, 3)
print np.hsplit(A, 2)
