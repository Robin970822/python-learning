import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A, B))
D = np.hstack((A, B))
print C
print A.shape, C.shape
print D
print A.shape, D.shape

# make vector A to matrix
print A[np.newaxis, :]
print A[np.newaxis, :].shape
print A[:, np.newaxis]
print A[:, np.newaxis].shape

# inverse the vector
A = A[:, np.newaxis]
B = B[:, np.newaxis]

C = np.vstack((A, B))
D = np.hstack((A, B))

print C
print D

C = np.concatenate((A, B, B, A), axis=0)
print C
D = np.concatenate((A, B, B, A), axis=1)
print D
A = A[:, np.newaxis]
B = B[:, np.newaxis]
E = np.concatenate((A, B, B, A), axis=2)
print A, A.shape
print B, B.shape
print E
