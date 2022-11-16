import json
from datetime import datetime

file1 = open("energyData.json")
file2 = open("priceData.json")

energyData = json.load(file1)
priceData = json.load(file2)

energyVals =[] 
priceVals = []
costVals = []
time_intervals = []

for i in energyData['energyData']:
    energyVals.append(i["EnergyUsage"])
    time_intervals.append(i["Timestamp"])

for i in priceData['priceData']:
    priceVals.append(i["Price"])

for i in range(len(priceVals)):
    costVals.append(priceVals[i] * energyVals[i])

cost_list = []
for time, cost in zip(time_intervals, costVals):
	cost_list.append({
		"Cost" : cost,

		"Timestamp" : time
	})

cost_dict = {"CostData" : cost_list }

with open("CostData.json", "w") as outfile:
	json.dump(cost_dict, outfile)

