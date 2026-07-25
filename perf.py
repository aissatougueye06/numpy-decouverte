import numpy as np
import time

n = 5_000_000

# Version Python pur — une boucle
liste = list(range(n))
debut = time.time()
resultat_liste = [x * 2 for x in liste]
print(f"Python pur : {time.time() - debut:.3f} s")

# Version NumPy — vectorisée
tableau = np.arange(n)
debut = time.time()
resultat_np = tableau * 2
print(f"NumPy      : {time.time() - debut:.3f} s")