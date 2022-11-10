import requests
import json
import hashlib
import datetime
url = "https://www.realtime-online.com/api/v3/json/"
token = "b30a7d8f6f92"
secretKey = "ATGUAP!Data2211"

#above variables are the token and secret key we were given for the API.

#ask user to enter system ID to get associated sensors.

sensorIds = input("What sensor(s) from the same system would you like the past 24 hour data for?\n If multiple please separate with a space.\n")
sensorIds = sensorIds.split(" ")
systemId = input("What system do these belong to?\n")


#if multiple sensors are requested, loop through each to create appropriate input
sensorList = []

for sensor in sensorIds:
    sensorList.append(
         {
 "sensor_id": sensor,
 #start date is 24 hours before current date.
 "start_date": (datetime.datetime.today() - datetime.timedelta(days=1)).isoformat(),
 "end_date": datetime.datetime.now().isoformat()
 }

    )


# Form the request, in this example, getting all the sensors associated with a chosen system.
request_body = {
 "action": "getSensorRecords",
 "request_date": datetime.datetime.now().isoformat(),
 "systems": [
 {
    #system id is stored as an int, whereas sensor id is a string... Of course...
 "system_id": int(systemId),
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

for i in range(len(sensorIds)):
    dataFor24hr = jsonResp["systems"][0]["sensors"][i]["data"]

    with open("../../web-app/src/data/24hrData/" + sensorIds[i] + "_24hrData.json", "w") as outfile:
        json.dump(dataFor24hr, outfile, indent = 2)
    


