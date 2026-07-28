import numpy as np

A = np.arange(15)
print(A)
print(A.shape)
print(A.reshape(15,1))


B = A.reshape(3,5)
print(B)
print(B.shape)
print(B.T)

print(np.zeros((3,5)))
print(np.ones((3,5)))
