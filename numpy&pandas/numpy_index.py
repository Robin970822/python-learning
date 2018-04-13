import numpy as np

A = np.arange(3, 15)
print A[3]

A = np.arange(3, 15).reshape((3, 4))
print A[2]

print A[1][1]
print A[1, 1]
# [1,3)
print A[1, 1:3]

for row in A:
    print row

for column in A.T:
    print column

print A.flatten()

for item in A.flat:
    print item
