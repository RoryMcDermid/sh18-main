import requests
import json
import hashlib
import datetime

def get_sensors_by_system(system_ids):
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    # above variables are the token and secret key we were given for the API.

    # Form the request, in this example, getting all the sensors associated with a chosen system.
    request_body = {
    "action": "getSensors",
    "request_date": datetime.datetime.now().isoformat(),
    "systems" : system_ids
    }

    # This bit here I just copied from their example python request.
    # magic string really is a descriptive variable as I have no idea what this does.

    magicString = json.dumps(request_body) + secretKey
    contentHash = hashlib.sha256(magicString.encode()).hexdigest()
    headers = {
    "X-RT2-API-Token": token,
    "X-RT2-API-Hash": contentHash
    }

    # post the above request to the API, then store the response in the jsonResp file.
    resp = requests.post(url, data=json.dumps(request_body), headers=headers)
    jsonResp = json.loads(resp.text)

    # store the reutrned response with all data (at the moment), that comes back.
    if jsonResp["status"] == 429:
        raise Exception("Timeout error, you have to wait 10 mins")


    sensorsBySystem = {}

    for sensor in jsonResp["sensors"]:
        if sensor["system_id"] not in sensorsBySystem.keys():
            sensorsBySystem[sensor['system_id']] = []
        sensorsBySystem[sensor['system_id']].append(sensor)
    

    return sensorsBySystem