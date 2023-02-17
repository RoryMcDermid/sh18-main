import numpy as np

def calculate_baseline(dataset) -> np.array:
    year_data = dataset.copy()
    # replace all zero values with NaN 
    # and find the minimum of all valid values (i.e non-NaN values) in each column
    year_data[year_data == 0] = np.nan
    col_mins = np.nanmin(year_data, axis=0)

    mean = np.mean(col_mins)
    std = np.std(col_mins)

    # defines upper and lower bounds to identify outliers 
    # as 2 standard deviations above and below the mean
    upper_bound = mean+(2*std)
    lower_bound = mean-(2*std)
    
    # finds values that are outside the upper or lower bounds 
    # and replaces them with the mean value
    col_mins[(lower_bound > col_mins) | (col_mins > upper_bound)] = mean
    
    return col_mins

