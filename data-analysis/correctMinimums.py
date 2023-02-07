import numpy as np

def correct_minimums(dataset) -> np.array:
    year_data = dataset.copy()
    year_data_corrected = year_data.copy()

    # replace all zero values with NaN 
    # and find the minimum of all valid values (i.e non-NaN values) in each column
    # we then broadcast the minimum values array to be the same shape as the original array
    year_data[year_data == 0] = np.nan
    col_extreme_mins = np.nanmin(year_data, axis=0)
    col_percentile = np.nanpercentile(year_data, 10, axis=0)
    col_mins = np.maximum(col_extreme_mins, col_percentile) # <-- this is the baseline readings we need
    col_mins_repeated = np.array([col_mins] * 364)

    # -----------

    # create a mask of all the values which are 0 in the original array 
    # to replace them with the calculated minimum values from above
    zeros_mask = year_data_corrected == 0
    year_data_corrected[zeros_mask] = year_data_corrected[zeros_mask] + col_mins_repeated[zeros_mask]

    return year_data_corrected
