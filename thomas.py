import numpy as np
from warnings import warn

# Resolve um sistema tridiagonal da forma Ax = d onde A é uma matriz triagonal
def solve_tridiag(A: np.ndarray, b_vec: np.ndarray) -> np.ndarray:
    n = len(A)
    a = np.array([A[i][i-1] for i in range(1, n)])
    b = np.array([A[i][i] for i in range(n)])
    c = np.array([A[i][i+1] for i in range(n-1)])

    # Cópia profunda do vetor b_vec
    d = np.array([i for i in b_vec], dtype= float)

    x = np.zeros(n)

    try:
        c[0] = c[0] / b[0]
        d[0] = d[0] / b[0]
    except ZeroDivisionError:
        warn(f'Divisão por zero no índice 0 da matriz b')
        raise ZeroDivisionError
    
    
    for i in range(1, n-1):
        try:
            div = (b[i] - a[i-1] * c[i-1])
            c[i] = c[i] / div
            d[i] = (d[i] - (a[i-1] * d[i-1])) / div
            
        except ZeroDivisionError:
            warn(f'Divisão por zero no índice {i} da matriz b')
            raise ZeroDivisionError
    
    try:
        d[n-1] = (d[n-1] - (a[n-2] * d[n-2])) / (b[n-1] - a[n-2] * c[n-2])
    
    except ZeroDivisionError:
        warn(f'Divisão por zero no índice {i} da matriz b')
        raise ZeroDivisionError

    x[-1] = d[-1]

    for i in range(n-2, -1, -1):
        x[i] = d[i] - c[i] * x[i+1]
    
    return x