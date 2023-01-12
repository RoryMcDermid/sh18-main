import requests
import json
import hashlib
import datetime as dt
import mysql.connector


#This function takes in two dates, as a string in the form of dd/mm/yyyy, then
#gets the values recordef by sensor 6311171 from system 2542, and parses the
#returned json by then returning a list of dicts that store a datetime value
#and the recorded data at that time.
#The dates are from midnight of the current time, so 01/01/1999 to 02/01/1999
# will return all data values recorded on 01/01/1999.

def getDatafromDates(start_date, end_date, systems_with_sensors_dict):
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    #above variables are the token and secret key we were given for the API.

    #if multiple sensors are requested, loop through each to create appropriate input

    formatted_systems = []

    start_date = start_date.isoformat()
    end_date = end_date.isoformat()

    for system in systems_with_sensors_dict.keys():
        sensor_list = []
        for sensor_id in systems_with_sensors_dict[system]:
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


    #looping over the data for each sensor listed, work your way down the json response until
    #required data is found, then store it in an appropriately named json file.


    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "moxie_energy"
     )
    cursor = mydb.cursor()

    sensors_dates_and_vals = {}
    
    for i in range(len(jsonResp["systems"])):
        system_id = jsonResp["systems"][i]["system_id"]
        for j in range(len(jsonResp["systems"][i]["sensors"])):
            readings = jsonResp["systems"][i]["sensors"][j]["data"]
            sensor_id = jsonResp["systems"][i]["sensors"][j]["sensor_id"]
            dates_and_vals = []
            cursor.execute(f"SELECT SENSOR_MEASUREMENT FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = {sensor_id}")
            sensor_measurement = cursor.fetchall()[0][0]
        

            for vals in readings:
                val_date = dt.datetime.strptime(vals["record_date"][0:19], "%Y-%m-%dT%H:%M:%S")
                try:
                    val_reading = vals["values"][sensor_measurement]
                except: 
                    val_reading = 0.00
                dates_and_vals.append({"date": val_date, "reading": val_reading})
            sensors_dates_and_vals[sensor_id] = dates_and_vals

    return sensors_dates_and_vals