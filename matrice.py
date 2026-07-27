import numpy as np

M = np.array([[1, 2, 3],
              [4, 5, 6]])

print(M)
print(M.shape)   # (2, 3) — 2 lignes, 3 colonnes
print(M.ndim)    # 2 — nombre de dimensions
print(M.size)    # 6 — nombre total d'éléments

print(np.zeros((2, 3)))       # matrice 2×3 de zéros
print(np.ones((3, 3)))        # matrice 3×3 de uns
print(np.eye(3))              # matrice identité 3×3
print(np.arange(12))          # [0, 1, 2, ..., 11]
print(np.arange(12).reshape(3, 4))   # les mêmes 12 valeurs, réarrangées en 3×4