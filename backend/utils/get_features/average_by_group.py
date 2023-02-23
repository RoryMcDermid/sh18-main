import datetime as dt
from typing import List
import numpy as np
from calendar import monthrange, isleap


def get_year_length(year):
    return 366 if isleap(year) else 365


def pad_data(dataset: List[List[str, float]]) -> List[List[str, float]]:
    start_date = dt.datetime.strptime(dataset[0][0], "%Y-%m-%dT%H:%M:%S")
    end_date = dt.datetime.strptime(dataset[-1][0], "%Y-%m-%dT%H:%M:%S")
    start_yday = start_date.timetuple().tm_yday
    end_yday = end_date.timetuple().tm_yday

    year_first = dt.datetime.strptime(f"{start_date.year}-01-01", "%Y-%m-%d")
    start_padding = [[year_first + dt.timedelta(days=i), np.NaN] for i in range(start_yday)]

    year_last = dt.datetime.strptime(f"{end_date.year}-12-31", "%Y-%m-%d")
    year_last_yday = year_last.timetuple().tm_yday
    end_padding = [[end_date + dt.timedelta(days=i), np.NaN] for i in range(year_last_yday - end_yday)]

    padded_dataset = np.hstack((start_padding, dataset, end_padding))
    return padded_dataset


def split_into_years(dataset: List[List[str, float]]) -> List[List[List[str, float]]]:
    start_date = dt.datetime.strptime(dataset[0][0], "%Y-%m-%dT%H:%M:%S")
    end_date = dt.datetime.strptime(dataset[-1][0], "%Y-%m-%dT%H:%M:%S")
    year_lengths = [get_year_length(y) for y in range(start_date.year, end_date.year)]
    result = np.split(dataset, np.cumsum(year_lengths)[:-1])
    return result


def split_and_format_into_months(year_dataset: List[str, float]) -> List[List[str, float]]:
    year = dt.datetime.strptime(year_dataset[0], "%Y-%m-%dT%H:%M:%S").year
    month_info = [monthrange(year, i) for i in range(12)]
    month_groups = np.split(year_dataset, np.cumsum(map(lambda x: x[1], month_info))[:-1])

    padded_month_blocks = []
    for start_weekday, month_data in zip(map(lambda x: x[0], month_info), month_groups):
        start_padding = np.full(start_weekday, np.NaN)
        end_pad_size = 7 - ((month_data.size + start_weekday) % 7)
        end_padding = np.full(end_pad_size, np.NaN)
        padded_month_blocks.append(np.hstack((start_padding, month_data, end_padding)))

    return padded_month_blocks


def get_average_by_group(dataset, date_string):
    month_idx = dt.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S").month - 1

    padded_dataset = pad_data(dataset)
    year_split_dataset = split_into_years(padded_dataset)

    month_blocks = []
    for year in year_split_dataset:
        month_blocks.append(split_and_format_into_months(year)[month_idx])

    month_blocks_arr = np.array(month_blocks)
    print(month_blocks_arr.shape)
