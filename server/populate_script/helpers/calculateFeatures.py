import datetime as dt
import numpy as np
from getDataForBaseline import *
def calculateFeatures(formatted_vals):
    mean = 0
    features_per_time_slot = {}
    formatted_numpy_vals = np.array(formatted_vals)
    formatted_numpy_vals.reshape(96, 365)
    print(formatted_numpy_vals)

yesterday_pre_midnight = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(minutes=15)
year_ago = yesterday_pre_midnight - dt.timedelta(days=1)

d_v_15_min = []
readings = getDataForBaseline(yesterday_pre_midnight, year_ago, {2417: ["6313133"]})
for vals in readings["systems"][0]["sensors"][0]["data"]:
    val_date = dt.datetime.strptime(vals["record_date"][0:19], "%Y-%m-%dT%H:%M:%S")
    try:
        val_reading = vals["values"]["pulse_count"]
    except: 
        val_reading = 0.00

    appropriate_time_intervals = ["00:00", "15:00", "30:00", "45:00"]
    if val_date.strftime("%M:%S") in appropriate_time_intervals:

        d_v_15_min.append((val_date, val_reading))

calculateFeatures(d_v_15_min)

