import numpy as np
from functions.kMeans import k_means
from functions.createCostMatrix import create_cost_matrix
from functions.normalise import normalise_to_probability_distribution
from functions import sinkhorn
from plotters import create_heatmap

# The goal of the optimal transport algorithm is to find the mapping that
# transforms the source distribution into the target distribution with the
# minimum amount of cost

def optimal_transport_test():
    # test source array to be passed through algorithm
    source = np.array([1, 10, 6, 9, 2, 4, 4, 1, 1, 7, 8, 9, 2, 3, 4, 5])

    centroids, clusters = k_means(source, 2)

    # mock target where expensive region is near the start 
    target = [*clusters[np.argmax(centroids)], *clusters[np.argmin(centroids)]]


    normalised_source = normalise_to_probability_distribution(source)
    normalised_target = normalise_to_probability_distribution(target)

    M = create_cost_matrix(normalised_source, normalised_target)

    heatmap_data = sinkhorn(normalised_source, normalised_target, M)

    create_heatmap(heatmap_data)


