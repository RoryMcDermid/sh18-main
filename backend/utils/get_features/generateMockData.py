import numpy as np
import datetime as dt


def get_date_boundaries(dataset):
    start_date = dt.datetime.strptime(dataset[0][0], "%Y-%m-%dT%H:%M:%S")
    end_date = dt.datetime.strptime(dataset[-1][0], "%Y-%m-%dT%H:%M:%S")
    return start_date, end_date


def generate_mock_data_naive(input_dataset, num_of_years=10):
    # TODO: make function work with incorrect input (like the one used in testing which does not start at 00:00)
    cut_off = len(input_dataset) % 96
    dataset = np.array(input_dataset[:-cut_off])

    start_date, end_date = get_date_boundaries(dataset)
    print(f"start_date: {start_date}")
    mock_start_date = dt.datetime(
        end_date.year - num_of_years,
        end_date.month,
        end_date.day,
        start_date.hour,
        start_date.minute,
        start_date.second,
    )
    padded_data_size = abs(mock_start_date - start_date).days
    num_of_new_timestamps = padded_data_size * 96

    timestamps = dataset[:, 0]
    energy_usage = dataset[:, 1].astype(np.float64)

    energy_usage = np.reshape(energy_usage, (-1, 96))
    mu_arr = np.mean(energy_usage, axis=0)
    sigma_arr = np.std(energy_usage, axis=0)

    mock_datetimes = [mock_start_date + dt.timedelta(minutes=i * 15) for i in range(num_of_new_timestamps - 1, -1, -1)]
    mock_timestamps = list(map(lambda x: dt.datetime.strftime(x, "%Y-%m-%dT%H:%M:%S"), mock_datetimes))

    mock_energy_usage = np.random.normal(mu_arr, sigma_arr, size=(padded_data_size, 96))

    final_timestamps = np.array(mock_timestamps + list(timestamps))
    final_energy_usage = np.vstack((mock_energy_usage, energy_usage)).reshape(-1)

    mock_dataset = [list(row) for row in zip(final_timestamps, final_energy_usage)]

    return mock_dataset
