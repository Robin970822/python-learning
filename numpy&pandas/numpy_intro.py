import numpy as np

array = np.array([[1, 2, 3], [2, 3, 4]])
print array
print 'number of dim:', array.ndim
print 'shape:', array.shape
print 'size:', array.size

a = np.arange(10, 20, 2)
print a

a = np.arange(12).reshape((3,4))
print a

a = np.linspace(1, 10, 20)
print a

a = a.reshape((5, 4))
print a