import numpy as np
import random

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