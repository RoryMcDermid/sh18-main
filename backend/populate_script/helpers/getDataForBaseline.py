import requests
import json
import hashlib
import datetime as dt

def getDataForBaseline(start_date, end_date, systems_with_sensors_dict):
    
#---------- CODE INSIDE THIS DASHED BLOCK IS A SPECIFIC REALTIME API CALL ------------#
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
    
    return jsonResp
    