import numpy as np

A = np.array([[2, 4], [1, 3], [0, 0], [0, 0]])

U, D, V = np.linalg.svd(A)

print U
print D
print V
