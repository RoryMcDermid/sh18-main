import pandas as pd
import numpy as np

def get_rows_with_mins(dataset) -> np.array:
    year_data = dataset.copy()

    # print(year_data[:200:20])    
    
    zeros_in_row = 96 - np.count_nonzero(year_data, axis=1)

    print('number of zeros in each row\n \
        (i.e number of timepoints in a day when the sensor was off)\n')
    print(zeros_in_row)

    df = pd.DataFrame(zeros_in_row, columns=['zeros_in_row'])


    
    # year_data[year_data == 0] = np.nan
    # min_rows = np.nanargmin(year_data, axis=0)

    # distinct_rows = set(min_rows)


    # df2 = pd.DataFrame(zeros_in_row)
    # # df = pd.DataFrame(min_rows, columns=['row_indices'])
    # df2['zeros_count'] = zeros_in_row

    # df2 = df2.loc[df2['zeros_count']==0]
    # print(df2)

