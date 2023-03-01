import requests
import json
import hashlib
import datetime as dt
from helpers.addReadings import *

# Taking 2 formatted date values, parse data of sensors and
# add to appropriate "READINGS_FOR_{sensor_id}" table.

def addDatafromDates(start_date, end_date, systems_with_list_of_sensors, mydb, cursor, online=False):

#---------- CODE INSIDE THIS DASHED BLOCK IS A SPECIFIC REALTIME API CALL ------------#
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    #above variables are the token and secret key we were given for the API.
    #if multiple sensors are requested, loop through each to create appropriate input
    formatted_systems = []

    start_date = start_date.isoformat()
    end_date = end_date.isoformat()

    for system, sensors in systems_with_list_of_sensors.items():
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

#--------------------------------------------------------------------------------------------#
    for i in range(len(jsonResp["systems"])):

        system_id = jsonResp["systems"][i]["system_id"]
        for j in range(len(jsonResp["systems"][i]["sensors"])):

            readings = jsonResp["systems"][i]["sensors"][j]["data"]
            sensor_id = jsonResp["systems"][i]["sensors"][j]["sensor_id"]

            cursor.execute(f"SELECT SENSOR_MEASUREMENT FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = '{sensor_id}'")
            sensor_measurement = cursor.fetchall()[0][0]
        
            if len(readings) > 0:

                cursor.execute(f"""CREATE TABLE READINGS_FOR_{sensor_id}(
                                READING_DATE DATE NOT NULL,
                                READING_TIME TIME NOT NULL, 
                                VALUE DECIMAL(15,6) NOT NULL)""")
                d_v_15_min = []
                rolling_sum = 0.0

                for vals in readings:
                    val_date = dt.datetime.strptime(vals["record_date"][0:19], "%Y-%m-%dT%H:%M:%S")
                    try:
                        val_reading = vals["values"][sensor_measurement]
                    except: 
                        val_reading = 0.00

                    appropriate_time_intervals = ["00:00", "15:00", "30:00", "45:00"]
                    if val_date.strftime("%M:%S") in appropriate_time_intervals:
                        d_v_15_min.append((val_date.date(), val_date.time(), val_reading))
                        rolling_sum = rolling_sum + val_reading

                if rolling_sum > 0:
                    addReadings(sensor_id, d_v_15_min, mydb, cursor)
                else:
                    cursor.execute(f"DROP TABLE READINGS_FOR_{sensor_id}")
                    cursor.execute(f"DELETE FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = '{sensor_id}'")
                    mydb.commit()
                    cursor.execute(f"SELECT * FROM SENSORS_FOR_{system_id}")
                    remaining_sensors = cursor.fetchall()
                    if len(remaining_sensors) == 0:
                        cursor.execute(f"DROP TABLE SENSORS_FOR_{system_id}")
                        cursor.execute(f"DELETE FROM SYSTEMS WHERE SYSTEM_ID = {system_id}")
                        mydb.commit()

            else:
                cursor.execute(f"DELETE FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = '{sensor_id}'")
                mydb.commit()
                cursor.execute(f"SELECT * FROM SENSORS_FOR_{system_id}")
                remaining_sensors = cursor.fetchall()
                if len(remaining_sensors) == 0:
                        cursor.execute(f"DROP TABLE SENSORS_FOR_{system_id}")
                        cursor.execute(f"DELETE FROM SYSTEMS WHERE SYSTEM_ID = {system_id}")
                        mydb.commit()