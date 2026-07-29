import numpy as np

a = np.array([3, 8, 1, 9, 4, 7, 12, 2])
print(a > 5)
print(a[a > 5])
print((a > 5).sum())

print(a[a % 2 == 0])

notes = np.array([12, 8, 15, 6, 17, 13])
noms  = np.array(["Ana", "Bob", "Cléo", "Dan", "Eve", "Sanchez"])

print(noms[(notes >= 10) & (notes <= 15)])  

print(a[a > 100])
print(a[a > 100].shape)