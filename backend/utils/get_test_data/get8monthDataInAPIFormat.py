import json
import requests
import datetime as dt
import hashlib

url = "https://www.realtime-online.com/api/v3/json/"
token = "b30a7d8f6f92"
secretKey = "ATGUAP!Data2211"

    #above variables are the token and secret key we were given for the API.
    #if multiple sensors are requested, loop through each to create appropriate input
formatted_systems = []

today = dt.date.today()
setup_end_date = dt.datetime.combine(today, dt.datetime.min.time()) - dt.timedelta(minutes=1)
setup_start_date = setup_end_date - dt.timedelta(weeks=32)

sensor_list = []
sensors = ["6313131"]
for sensor_id in sensors:
    sensor_list.append(
        {
        "sensor_id": sensor_id,
        "start_date": setup_start_date.isoformat(),
        "end_date": setup_end_date.isoformat()
        }
        )
formatted_systems.append(
        {
    "system_id": 2418,
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

readings = jsonResp["systems"][0]["sensors"][0]["data"]
sensor_measurement = "pulse_count"
in_api_format = []
for val in readings:
    val_date = val["record_date"][0:19]
    val_reading = val["values"][sensor_measurement]
    in_api_format.append([val_date, val_reading])

with open(f"eightMonthsData{sensors[0]}.json", "w") as f:
    json.dump(in_api_format, f)
