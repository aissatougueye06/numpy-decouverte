import numpy as np

notes = np.array([12, 8, 15, 6, 17])
noms  = np.array(["Ana", "Bob", "Cléo", "Dan", "Eve"])

print(noms[notes >= 10])   # ['Ana' 'Cléo' 'Eve']