import requests
import json
import hashlib
import datetime as dt

#This function takes in two dates, as a string in the form of dd/mm/yyyy, then
#gets the values recordef by sensor 6311171 from system 2542, and parses the
#returned json by then returning a list of dicts that store a datetime value
#and the recorded data at that time.
#The dates are from midnight of the current time, so 01/01/1999 to 02/01/1999
# will return all data values recorded on 01/01/1999.

def getDatafromDates(start_date, end_date):
    url = "https://www.realtime-online.com/api/v3/json/"
    token = "b30a7d8f6f92"
    secretKey = "ATGUAP!Data2211"

    #above variables are the token and secret key we were given for the API.

    #if multiple sensors are requested, loop through each to create appropriate input
    sensorList = []

    start_date = start_date.isoformat()
    end_date = end_date.isoformat()

    sensorList.append(
        {
    "sensor_id": "6311171",
    "start_date": start_date,
    "end_date": end_date
    }
    )


    # Form the request, in this example, getting all the sensors associated with a chosen system.
    request_body = {
    "action": "getSensorRecords",
    "request_date": dt.datetime.now().isoformat(),
    "systems": [
    {
        #system id is stored as an int, whereas sensor id is a string... Of course...
    "system_id": 2542,
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

    #clean up response json here.

    readings = jsonResp["systems"][0]["sensors"][0]["data"]
    dates_and_vals = []

    for vals in readings:
        val_date = dt.datetime.strptime(vals["record_date"][0:19], "%Y-%m-%dT%H:%M:%S")
        val_reading = vals["values"]["pulse_count"]
        dates_and_vals.append({"date": val_date, "reading": val_reading})

    return dates_and_vals