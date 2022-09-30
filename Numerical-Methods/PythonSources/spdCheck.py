import numpy as np

# Return true if matrix is symmetric
def symmetricCheck(A):
    return (A==A.T).all()

# Return true if all eigenvals are positive
def isSymmetricPositiveDefinite(A):
    if(symmetricCheck(A)):
        return np.all(np.linalg.eigvals(A) > 0)
