import pandas as pd
import numpy as np
import json

#read in entire excel file to a pandas dataframe selects only data for 1 day
energy_df = pd.read_excel('UniElec092022.xlsx', sheet_name = 1).iloc[::30, :]

# print(energy_df)

mean_usage = energy_df['total'].values / 48

peak_usage = energy_df.iloc[:, 35:41].mean(axis=1).values

# print(mean_usage < peak_usage)

# print(mean_usage)

# mean_usage['mean'] = mean_usage['total']


#taking the columns headers of the new dataframe, select only the time components
time_intervals = list(energy_df.columns)[3:]

# print(energy_df)

def is_expensive(row):
	peak_avg = row[32:38].mean()
	p_50 = np.percentile(row, 65)
	p_75 = np.percentile(row, 85)
	if (peak_avg > p_75): return 'expensive'
	if (peak_avg > p_50): return 'somewhat expensive'
	return 'not expensive'

expensive_status = {}
for i in range(23):
	single_row = energy_df.iloc[i][3:].values
	expensive_status["serialNo" + str(i)] = is_expensive(single_row)


# writing the data into a file
with open("../../web-app/src/data/building_ExpStatus.json", "w") as out:
	json.dump(expensive_status, out, indent = 2)
