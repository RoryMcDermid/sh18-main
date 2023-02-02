from loadData import load_from_file
import pandas as pd
import numpy as np

def calculate_baseline(sensor_id):
    sensor_data = load_from_file(sensor_id=sensor_id)

    df = pd.DataFrame(sensor_data)
    df['values'] = df['values'].map(lambda x: x['pulse_count'])

    # at this point `df` is a dataframe with 34_944 rows (364 days, 96 timepoints)
    # and 2 columns (timestamp: record_date, value: values)

    # -----------

    # `year_data` is a 2D array where each row represents a single day in a year long period
    # and each column represents a timepoint in a day
    year_data = np.reshape(df['values'].values, (364, 96))

    # -----------

    # replace all zero values with NaN 
    # and find the minimum of all valid values (i.e non-NaN values) in each column
    year_data[year_data == 0] = np.nan
    return np.nanmin(year_data, axis=0)
