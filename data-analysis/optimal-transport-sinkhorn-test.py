import numpy as np
import matplotlib.pyplot as plt
import random

# The goal of the optimal transport algorithm is to find the mapping that
# transforms the source distribution into the target distribution with the
# minimum amount of cost


def k_means(data, k, max_iterations=1000):
    # Initialize the centroids randomly
    centroids = [data[i] for i in random.sample(range(len(data)), k)]

    for _ in range(max_iterations):
        # Initialize lists to store the elements assigned to each cluster
        clusters = [[] for i in range(k)]

        # Assign each element to the closest centroid
        for element in data:
            distances = [np.linalg.norm(element - centroid)
                         for centroid in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(element)

        # Recalculate the centroids as the mean of the elements in each cluster
        for i in range(k):
            centroids[i] = np.mean(clusters[i], axis=0)

    return centroids, clusters


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


source = np.array([1, 10, 6, 9, 2, 4, 4, 1, 1, 7, 8, 9, 2, 3, 4, 5])

centroids, clusters = k_means(source, 2)
print(*clusters)

target = [*clusters[np.argmax(centroids)], *clusters[np.argmin(centroids)]]
print(target)

source = normalize_to_probability_distribution(source)
target = normalize_to_probability_distribution(target)

M = create_cost_matrix(source, target)

result = sinkhorn(source, target, M)

plt.imshow(result, cmap='hot')
plt.title('Heatmap of Transport Matrix')
plt.xlabel('target indexes')
plt.ylabel('source indexes')
plt.show()
