import pandas as pd
import numpy as np
import json

#read in entire excel file to a pandas dataframe
energy_file = pd.read_excel('UniElec092022.xlsx', sheet_name = 1)

#taking the columns headers of the new dataframe, select only the time components
time_intervals = list(energy_file.columns)[3:]

#select the values of the dataframe making a numpy array in the process
as_nparray = energy_file.values

#select the serial numbers of the AMRs
serialNos = as_nparray[1::30, 0]


#slice the np array to get the first of september 24 usage for each AMR
first_sep_vals = as_nparray[::30, 3:]

data_dict = {}
for i in range(len(serialNos)):
	data_list = []
	for time, energy in zip(time_intervals, first_sep_vals[i]):
		data_list.append({
			"EnergyUsage" : energy,
			"Timestamp" : time.strftime("%H:%M")
		})
	data_dict["serialNo" + str(i)] = data_list

# writing the data into the file
with open("../../web-app/src/data/energyDataAllAMR.json", "w") as outfile:
	json.dump(data_dict, outfile, indent = 2)
