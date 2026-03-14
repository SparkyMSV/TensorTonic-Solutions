import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m = len(A)
    n = len(A[0])
    fin = []
    for i in range(n):
        r = []
        for j in range(m):
            r.append(A[j][i])
        fin.append(r)
    return np.array(fin)
