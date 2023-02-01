import numpy as np
import matplotlib.pyplot as plt

# The goal of the optimal transport algorithm is to find the mapping that
# transforms the source distribution into the target distribution with the
# minimum amount of cost

# problem: how do we determine the target distribution in our application ????


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


source = np.array([1, 10, 6, 9, 2, 4, 4, 0, 0, 7, 8, 9, 3, 1, 2])
target = np.array([1, 5, 0, 0, 0, 9, 10, 3, 5, 6, 2, 1, 6, 7, 1])


source = normalize_to_probability_distribution(source)
target = normalize_to_probability_distribution(target)

M = create_cost_matrix(source, target)

result = sinkhorn(source, target, M)

plt.imshow(result, cmap='hot')
plt.title('Heatmap of Transport Matrix')
plt.xlabel('target indexes')
plt.ylabel('source indexes')
plt.show()
