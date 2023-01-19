from getSensorList import *
import json



f = open("getSensors.json", "w")
g = list(dict(json.load(open("system_ids.json", "r"))).keys())
x = getSensors(g)
json.dump(x, f)