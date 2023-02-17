import numpy as np


def correct_minimums(dataset) -> np.array:
    year_data = dataset.copy()
    year_data_corrected = year_data.copy()

    # replace all zero values with NaN
    # and find the minimum of all valid values (i.e non-NaN values) in each column
    year_data[year_data == 0] = np.nan
    col_mins = np.nanpercentile(year_data, 5, axis=0)

    # we then broadcast the minimum values array to be the same shape as the original array
    col_mins_repeated = np.array([col_mins] * dataset.shape[0])

    # -----------

    # create a mask of all the values which are 0 in the original array
    # to replace them with the calculated minimum values from above
    zeros_mask = year_data_corrected == 0
    year_data_corrected[zeros_mask] = year_data_corrected[zeros_mask] + col_mins_repeated[zeros_mask]

    return year_data_corrected
