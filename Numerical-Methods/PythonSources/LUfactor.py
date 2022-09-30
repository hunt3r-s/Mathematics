# Adapted from https://docs.scipy.org/
from scipy.linalg import lu_factor, lu_solve
import numpy as np

A = np.array([1, 5, 2, 3, 6, 2, -2, 2, 1])
b = np.array([1,-1,3])
m = 3
n = 3

def linSysLU(A, b, m, n):
    A = A.reshape(m, n)
    lu, piv = lu_factor(A)
    
    # Solution to system
    x = lu_solve((lu, piv), b)
    return x
