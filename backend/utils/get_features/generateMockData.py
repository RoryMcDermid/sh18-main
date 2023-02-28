import numpy as np
import datetime as dt


def get_date_boundaries(dataset):
    start_date = dt.datetime.combine(
        dataset[0][0], dataset[0][1])
    end_date = dt.datetime.combine(
        dataset[-1][0], dataset[-1][1])
    return start_date, end_date


def trim_to_shape(dataset):
    start_date, end_date = get_date_boundaries(dataset)

    start_time_is_correct = start_date.hour == 0 and start_date.minute == 0
    end_time_is_correct = (end_date.hour == 23) and (end_date.minute == 45)
    if start_time_is_correct and end_time_is_correct:
        return dataset

    toal_delta = len(dataset) % 96

    last_date = dt.datetime(end_date.year, end_date.month,
                            end_date.day - 1, hour=23, minute=45, second=0)
    end_delta = abs((end_date - last_date) // dt.timedelta(minutes=15))

    start_delta = toal_delta - end_delta

    return dataset[start_delta:-end_delta]


def generate_mock_data(dataset, num_of_years=10):
    dataset = trim_to_shape(dataset)
    dataset = np.array(dataset)

    start_date, end_date = get_date_boundaries(dataset)
    mock_start_date = dt.datetime(
        end_date.year - num_of_years,
        end_date.month,
        end_date.day,
        start_date.hour,
        start_date.minute,
        start_date.second,
    )
    padded_data_size = abs(mock_start_date - start_date).days - 1
    num_of_new_timestamps = padded_data_size * 96

    timestamps = [dt.datetime.combine(
        datapoint[0], datapoint[1]) for datapoint in dataset]
    energy_usage = dataset[:, 2].astype(np.float64)

    energy_usage = np.reshape(energy_usage, (-1, 96))
    mu_arr = np.mean(energy_usage, axis=0)
    sigma_arr = np.std(energy_usage, axis=0)

    mock_datetimes = [
        mock_start_date + dt.timedelta(minutes=i * 15) for i in range(num_of_new_timestamps)]
    mock_timestamps = list(map(lambda x: dt.datetime.strftime(
        x, "%Y-%m-%dT%H:%M:%S"), mock_datetimes))

    mock_energy_usage = np.random.normal(
        mu_arr, sigma_arr, size=(padded_data_size, 96))

    final_timestamps = np.array(mock_timestamps + list(timestamps))
    final_energy_usage = np.vstack(
        (mock_energy_usage, energy_usage)).reshape(-1)

    mock_dataset = [list(row)
                    for row in zip(final_timestamps, final_energy_usage)]

    return mock_dataset
