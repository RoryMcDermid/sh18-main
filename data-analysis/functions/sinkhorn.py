import numpy as np


def sinkhorn(a, b, M, epsilon=0.1, max_iter=1000):
    n = a.shape[0]
    m = b.shape[0]
    K = np.exp(-M / epsilon)

    # Initialize u and v
    u = np.ones(n) / n
    v = np.ones(m) / m

    # Iterate until convergence
    for _ in range(max_iter):
        u = a / np.maximum(K @ (v / np.maximum(K.T @ u, 1e-10)), 1e-10)
        v = b / np.maximum(K.T @ (u / np.maximum(K @ v, 1e-10)), 1e-10)

    # Compute the transport matrix
    P = np.outer(u, v) * K

    return P