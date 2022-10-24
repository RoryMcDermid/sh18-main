import pandas as pd
import numpy as np
import json

energy_file = pd.read_excel('UniElec092022.xlsx', sheet_name = 1, usecols="D:AY")

#get all the values from first of september records
time_intervals = energy_file.columns

all_first_sep = energy_file.values[::30,]
num_rows, num_cols = all_first_sep.shape
avg_first_sep = np.mean(all_first_sep, axis=0)

energy_l = []


for i in range(48):
	temp = {}
	temp["Timestamp"] = time_intervals[i].strftime("%H:%M")
	temp["EnergyUsage"] = avg_first_sep[i]
	energy_l.append(temp)

energy_d = {}

energy_d["energyUsage"] = energy_l

with open("../../web-app/src/mock-data/usageData.json", "w") as outfile:
	json.dump(energy_d, outfile)




