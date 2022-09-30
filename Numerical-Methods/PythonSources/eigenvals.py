# eigenvals in Python
from numpy import linalg as LA
A = np.array([[-1, 1, 0], [-4, 3, 0], [1, 0, 2]])
# eigenvals are repeated according to multiplicity
def Eigenvalues(A):
    eigenvals, eigenvecs = LA.eig(A)
    return eigenvals, eigenvecs
