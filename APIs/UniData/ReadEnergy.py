import pandas as pd
import numpy as np
import json

energy_file = pd.read_excel('UniElec092022.xlsx', sheet_name = 1, usecols="D:AY")

# get all the values from first of september records
time_intervals = energy_file.columns

all_first_sep = energy_file.values[::30,]
avg_first_sep = np.mean(all_first_sep, axis=0)

data_list = []
for time, energy in zip(time_intervals, avg_first_sep):
	data_list.append({
		"EnergyUsage" : energy,
		"Timestamp" : time.strftime("%H:%M")
	})

data_dict = {"energyData" : data_list }

with open("../../web-app/src/mock-data/energyData.json", "w") as outfile:
	json.dump(data_dict, outfile)




