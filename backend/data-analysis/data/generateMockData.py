import numpy as np


def generate_mock_data_naive(arr, num_of_years=10):
    n = num_of_years * 365

    arr = np.reshape(arr, (-1, 96))
    mu_arr = np.mean(arr, axis=0)
    sigma_arr = np.std(arr, axis=0)

    mock_data_arr = np.random.normal(mu_arr, sigma_arr, size=(n, 96)).T
    return mock_data_arr
