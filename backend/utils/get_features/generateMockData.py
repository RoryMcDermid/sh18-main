import numpy as np
import datetime as dt

"""
[
    ["2022-01-01T00:00", 0.1223],
    ["2022-01-01T00:15", 0.1223],
    ["2022-01-01T00:30", 0.1223],
    ["2022-01-01T00:45", 0.1223],
    ["2022-01-01T01:00", 0.1223],
    ["2022-01-01T01:15", 0.1223],
    ["2022-01-01T01:30", 0.1223],
]

"""


# TODO: make function account for leap years
def generate_mock_data_naive(dataset, num_of_years=10):
    dataset = np.array(dataset, dtype=[("timestamp", "U19"), ("energy_usage", float)])

    # TODO: make this a helper function
    start_date = dt.datetime.strptime(dataset[0][0], "%Y-%m-%dT%H:%M:%S")
    end_date = dt.datetime.strptime(dataset[-1][0], "%Y-%m-%dT%H:%M:%S")

    padded_data_size = (dt.datetime(end_date.year - num_of_years, end_date.month, end_date.day) - start_date).days

    timestamps = dataset[:, 0]
    energy_usage = dataset[:, 1].astype(np.float64)

    # break 1

    energy_usage = np.reshape(energy_usage, (-1, 96))
    mu_arr = np.mean(energy_usage, axis=0)
    sigma_arr = np.std(energy_usage, axis=0)

    mock_timestamps = [
        dt.datetime.strftime(end_date - dt.timedelta(minutes=i * 15), "%Y-%m-%dT%H:%M")
        for i in range(padded_data_size - 1, -1, -1)
    ]
    mock_energy_usage = np.random.normal(mu_arr, sigma_arr, size=(padded_data_size, 96)).T

    # break 2

    final_timestamps = np.array(mock_timestamps + list(timestamps))
    final_energy_usage = np.concatenate((mock_energy_usage, energy_usage), axis=0).reshape(-1)

    mock_dataset = [list(row) for row in zip(final_timestamps, final_energy_usage)]

    return mock_dataset
