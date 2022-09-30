#LDL^T Factorization of a matrix
from scipy.linalg import ldl
import numpy as np

def llTranspose(A):
    lu, d, perm = ldl(A, lower=0)
    return(lu, d, lu.T)
