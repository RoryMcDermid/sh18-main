import numpy as np

def create_cost_matrix(a, b):
    a = a.reshape(-1, 1)
    b = b.reshape(1, -1)

    return np.sqrt((a - b) ** 2).T