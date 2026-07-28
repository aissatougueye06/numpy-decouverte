import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m.shape)
print(m[1,:])
print(m[:,2])

m2 = np.arange(12)
m3 = m2.reshape(3,4)
print(m2)
print(m3)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A * B)
print(A @ B)

C = np.arange(12).reshape(3, 4)
print(C.shape)
print(C.T)
print(C.T.shape)

D = np.array([100, 200, 300, 400])
print(C + D)

E = np.array([100, 200, 300])
print(C + E)
