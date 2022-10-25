import json

import requests

header = {
    'Authorization': 'Bearer 9c33ba709890474fa8711718795dfb74'
}


# # Create a blank form
# forms = requests.post(
#     "https://utilityapi.com/api/v2/forms",
#     headers=header,
# )
#
# uid = forms.json()["uid"]
# print("uid: "+ uid)
#
# # Simulate someone submitting an authorization
# testSubmit = requests.post(
#     'https://utilityapi.com/api/v2/forms/' + uid + '/test-submit',
#     headers=header,
#     data='{"utility": "PCE", "scenario": "commercial"}',
# )
#
# referral = testSubmit.json()['referral']
#
# print("referal: "+ referral)
#
# # Get Authorizations and Meters associated with the referral code
# createAuthorizationsAndMeters = requests.get(
#     'https://utilityapi.com/api/v2/authorizations?referrals=' + referral + '&include=meters',
#     headers=header,
# )
#
#
# meterUid = createAuthorizationsAndMeters.json()["authorizations"][0]["meters"]
# print(meterUid)

meters = requests.get(
     "https://utilityapi.com/api/v2/meters",
     headers=header,
 )

meter_intervals = meters.json()["meters"][0]["exports"]["intervals_csv"]

intervals = requests.get(
    "https://utilityapi.com/api/v2/intervals",
    params={'authorizations': "318018"},
    headers=header,
)

intervalReading = intervals.json()['intervals'][0]['readings']

energyList = []

for dic in intervalReading[::-2]:
    energyList.append({
        "EnergyUsage" : dic["kwh"],
        "Timestamp" : dic["start"][11:16]
    })

data_dict = {"energyData": energyList}

with open("../web-app/src/mock-data/utilityAPIEnergyData.json", "w") as outfile:
    json.dump(data_dict, outfile)
