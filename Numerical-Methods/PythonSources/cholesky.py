# Cholesky factorization in Python
from scipy.linalg import cholesky
import numpy as np

A = np.array([[2, 1], [1, 2]])
def CholeskyFactorization(A):
    L = cholesky(A, lower = True)
    Lt = L.T.conj()
    return(L,Lt)
