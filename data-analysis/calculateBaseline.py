import numpy as np

def calculate_baseline(dataset) -> np.array:
    year_data = dataset.copy()
    # replace all zero values with NaN 
    # and find the minimum of all valid values (i.e non-NaN values) in each column
    year_data[year_data == 0] = np.nan
    return np.nanpercentile(year_data, 10, axis=0)
