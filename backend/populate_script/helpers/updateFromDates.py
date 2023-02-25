import requests
import json
import hashlib
import datetime as dt
import mysql.connector
from helpers.addReadings import *

def updateFromDates(start_date, end_date, systems_with_sensors_dict, mydb, cursor, online=False):
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

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
    
    if online:
        reference_time = dt.datetime.now()

    for i in range(len(jsonResp["systems"])):
        system_id = jsonResp["systems"][i]["system_id"]
        for j in range(len(jsonResp["systems"][i]["sensors"])):

            if online:

                if (dt.datetime.now() - reference_time).total_seconds() > 8:
                    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
                    dotenv.load_dotenv(dotenv_path=env_path)

                    mydb = mysql.connector.connect(
                        username=os.environ.get('DB_USERNAME'),
                        host=os.environ.get('DB_HOST'),
                        password=os.environ.get('DB_PASSWORD'),
                        database=os.environ.get('DB')
                    )
                    cursor = mydb.cursor(buffered=True)
                    reference_time = dt.datetime.now()

            readings = jsonResp["systems"][i]["sensors"][j]["data"]
            sensor_id = jsonResp["systems"][i]["sensors"][j]["sensor_id"]

            cursor.execute(f"SELECT SENSOR_MEASUREMENT FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = {sensor_id}")
            sensor_measurement = cursor.fetchall()[0][0]
        
            if len(readings) > 0:
                d_v_15_min = []

                for vals in readings:
                    val_date = dt.datetime.strptime(vals["record_date"][0:19], "%Y-%m-%dT%H:%M:%S")
                    try:
                        val_reading = vals["values"][sensor_measurement]
                    except: 
                        val_reading = 0.00

                    appropriate_time_intervals = ["00:00", "15:00", "30:00", "45:00"]
                    if val_date.strftime("%M:%S") in appropriate_time_intervals:
                        d_v_15_min.append((val_date, val_reading))
                        
                addReadings(sensor_id, d_v_15_min, mydb, cursor, online)