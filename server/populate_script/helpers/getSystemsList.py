import requests
import json
import hashlib
import datetime


def getSystemsList():
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    # above variables are the token and secret key we were given for the API.

    # Form the request, in this example, getting all systems associated with the Uni.
    request_body = {
    "action": "getSystems",
    "request_date": datetime.datetime.now().isoformat(),

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

    if jsonResp["status"] == 429:
        raise Exception("Timeout error, you have to wait 10 mins")

    # Parse this file to store the system IDs, with their associated name and sensor count.

    listOfSystems = jsonResp["systems"]

    systemIds = {}

    for system in listOfSystems:
        systemIds[system["system_id"]] = {
            "name" : system["name"],
            "noOfSensors" : system["sensors_count"]
        }

    return systemIds