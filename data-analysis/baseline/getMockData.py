from helpers.getSensorList import getSensors
from helpers.getSystemsList import *

all_sensors = getSensors(getSystemsList())

print(len(all_sensors))
