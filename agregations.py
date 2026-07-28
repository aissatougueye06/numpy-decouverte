import numpy as np

C = np.arange(12).reshape(3, 4)
print(C.mean())  #moyenne globale
print(C.mean(axis=0))  #moyenne par colonne
print(C.mean(axis=0).shape)  #shape moyenne par colonne
print(C.mean(axis=1))  #moyenne par ligne
print(C.mean(axis=1).shape)  #shape moyenne par ligne

print(C.mean(axis=1)[0])    #moyenne étudiant 1
print(C.mean(axis=1)[1])    #moyenne étudiant 2
print(C.mean(axis=1)[2])    #moyenne étudiant 3

print(C.mean(axis=0)[0])    #moyenne matière 1
print(C.mean(axis=0)[1])    #moyenne matière 2
print(C.mean(axis=0)[2])    #moyenne matière 3
print(C.mean(axis=0)[3])    #moyenne matière 4

D = C - C.mean(axis=0)
print(D)
print(D.mean(axis=0))

print(C.mean(axis=1, keepdims=True))
E = C - C.mean(axis=1, keepdims=True)
print(E)