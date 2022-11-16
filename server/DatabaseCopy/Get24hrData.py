import requests
import json
import hashlib
import datetime as dt

def get24hrData(sensor_id, system_id):
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    #above variables are the token and secret key we were given for the API.

    #if multiple sensors are requested, loop through each to create appropriate input
    sensorList = []
    today = dt.datetime.today()
    yesterday = today - dt.timedelta(days=1)
    midnight = dt.datetime.min.time()

    start_date_midnight = dt.datetime.combine(yesterday, midnight).isoformat()
    end_date_midnight = dt.datetime.combine(today, midnight).isoformat()

    sensorList.append(
        {
    "sensor_id": sensor_id,
    #start date is day before current date at midnight.
    "start_date": start_date_midnight,
    "end_date": end_date_midnight
    }

        )


    # Form the request, in this example, getting all the sensors associated with a chosen system.
    request_body = {
    "action": "getSensorRecords",
    "request_date": dt.datetime.now().isoformat(),
    "systems": [
    {
        #system id is stored as an int, whereas sensor id is a string... Of course...
    "system_id": int(system_id),
    "sensors": sensorList
    }
    ]
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

    #looping over the data for each sensor listed, work your way down the json response until
    #required data is found, then store it in an appropriately named json file.

    return jsonResp
        


