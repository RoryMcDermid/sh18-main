import pandas as 
import matplotlib.pyplot as plt
import numpy as np 
import matplotlib.dates

energy_file = pd.read_excel('UniElec092022.xlsx', sheet_name = 1, usecols="B:C")

energy_list = energy_file.values.tolist()

x = energy_list[:30, 0]
y = energy_list[:30, 1]
dates = matplotlib.dates.date2num(x)


fig, ax = plt.subplots()

ax.plot(date, y, linewidth = 2.0)

plt.show()



