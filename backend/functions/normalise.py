import numpy as np

def normalise_to_probability_distribution(array):
    return array / np.sum(array)