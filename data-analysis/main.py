from baseline.correctMinimums import correct_minimums
from baseline.loadData import load_from_file
from baseline.createBoxplot import create_boxplot
import pandas as pd
import numpy as np

def main():
    sensor_data = load_from_file(sensor_id='6316312') 

    df = pd.DataFrame(sensor_data)
    df['values'] = df['values'].map(lambda x: x['pulse_count'])

    # at this point `df` is a dataframe with 34_944 rows (364 days, 96 timepoints)
    # and 2 columns (timestamp: record_date, value: values)

    # -----------

    # `year_data` is a 2D array where each row represents a single day in a year long period
    # and each column represents a timepoint in a day
    year_data = np.reshape(df['values'].values, (364, 96))

    corrected_dataset = correct_minimums(year_data)

    create_boxplot(corrected_dataset)





if __name__ == '__main__':
    main()