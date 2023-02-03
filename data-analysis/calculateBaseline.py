import numpy as np

def calculate_baseline(dataset):
    year_data = dataset.copy()
    # replace all zero values with NaN 
    # and find the minimum of all valid values (i.e non-NaN values) in each column
    year_data[year_data == 0] = np.nan
    return np.nanmin(year_data, axis=0)
