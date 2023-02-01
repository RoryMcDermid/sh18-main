import numpy as np
import matplotlib.pyplot as plt

# In this implementation, a is the source array and b is the target array

# The goal of the optimal transport algorithm is to find the mapping that
# transforms the source distribution into the target distribution with the
# minimum amount of cost


def normalize_to_probability_distribution(array):
    return array / np.sum(array)


def create_cost_matrix(a, b):
    a = a.reshape(-1, 1)
    b = b.reshape(1, -1)

    return np.sqrt((a - b) ** 2).T


def sinkhorn(a, b, M, epsilon=0.1, max_iter=1000):
    n = a.shape[0]
    m = b.shape[0]
    K = np.exp(-M / epsilon)

    # Initialize u and v
    u = np.ones(n) / n
    v = np.ones(m) / m

    # Iterate until convergence
    for i in range(max_iter):
        u = a / np.maximum(K @ (v / np.maximum(K.T @ u, 1e-10)), 1e-10)
        v = b / np.maximum(K.T @ (u / np.maximum(K @ v, 1e-10)), 1e-10)

    # Compute the transport matrix
    P = np.outer(u, v) * K

    return P


a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 0, 8])

a = normalize_to_probability_distribution(a)
b = normalize_to_probability_distribution(b)

M = create_cost_matrix(a, b)

result = sinkhorn(a, b, M)

plt.imshow(result, cmap='hot')
plt.show()
