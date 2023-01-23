import requests
import json
import hashlib
import datetime as dt
import mysql.connector
from helpers.addToIter import *
from helpers.deleteFromIter import *



def updateFromDates(start_date, end_date, systems_with_sensors_dict, mydb, cursor):
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    #above variables are the token and secret key we were given for the API.

    #if multiple sensors are requested, loop through each to create appropriate input

    formatted_systems = []

    start_date = start_date.isoformat()
    end_date = end_date.isoformat()

    for system, sensors in systems_with_sensors_dict.items():
        sensor_list = []
        for sensor_id in sensors:
            sensor_list.append(
            {
        "sensor_id": sensor_id,
        "start_date": start_date,
        "end_date": end_date
        }
        )
        formatted_systems.append(
            {
    "system_id": system,
    "sensors": sensor_list
    }
        )
    # Form the request, in this example, getting all the sensors associated with a chosen system.
    request_body = {
    "action": "getSensorRecords",
    "request_date": dt.datetime.now().isoformat(),
    "systems": formatted_systems
    }

    # This bit here I just copied from their example python request.
    # magic string really is a descriptive variable as I have no idea what this does.
    magicString = json.dumps(request_body) + secretKey
    contentHash = hashlib.sha256(magicString.encode()).hexdigest()
    headers = {
    "X-RT2-API-Token": token,
    "X-RT2-API-Hash": contentHash
    }

    #post the above request to the API, then store the response in the jsonResp file.
    resp = requests.post(url, data=json.dumps(request_body), headers=headers)
    jsonResp = json.loads(resp.text)


    if jsonResp["status"] == 429:
        raise Exception("Timeout error, you have to wait 10 mins")
    
    iter_vals = ["ITER_1", "ITER_2", "ITER_3", "iTER_4"]

    for i in range(len(jsonResp["systems"])):
        system_id = jsonResp["systems"][i]["system_id"]
        for j in range(len(jsonResp["systems"][i]["sensors"])):

            readings = jsonResp["systems"][i]["sensors"][j]["data"]
            sensor_id = jsonResp["systems"][i]["sensors"][j]["sensor_id"]

            cursor.execute(f"SELECT SENSOR_MEASUREMENT FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = {sensor_id}")
            sensor_measurement = cursor.fetchall()[0][0]
        
            if len(readings) > 0:
                d_v_15_min, d_v_1_hr, d_v_4_hr, d_v_1_day  = [], [], [], []
                hr_counter, four_hr_counter,day_counter = 0, 0, 0
                hr_sum, four_hr_sum, day_sum = 0.0, 0.0, 0.0
                for vals in readings:
                    val_date = dt.datetime.strptime(vals["record_date"][0:19], "%Y-%m-%dT%H:%M:%S")
                    try:
                        val_reading = vals["values"][sensor_measurement]
                    except: 
                        val_reading = 0.00

                    hr_sum = hr_sum + val_reading
                    four_hr_sum = four_hr_sum + val_reading
                    day_sum = day_sum + val_reading

                    hr_counter = hr_counter + 1
                    four_hr_counter = four_hr_counter + 1
                    day_counter = day_counter + 1

                    d_v_15_min.append((val_date, val_reading))
                    if hr_counter % 4 == 0:
                        d_v_1_hr.append((val_date, hr_sum))
                        hr_sum = 0.0
                    if four_hr_counter % 16 == 0:
                        d_v_4_hr.append((val_date, four_hr_sum))
                        four_hr_sum = 0.0
                    if day_counter % 96 == 0:
                        d_v_1_day.append((val_date, day_sum))
                        day_sum = 0.0

                formatted_dates_vals_list = [d_v_15_min, d_v_1_hr, d_v_4_hr, d_v_1_day]

                for iter_val, formatted_dates_vals in zip(iter_vals, formatted_dates_vals_list):
                    addToIter(sensor_id, iter_val, formatted_dates_vals, mydb, cursor)

            for iter_val in iter_vals:
                deleteFromIter(sensor_id, iter_val, mydb, cursor)
