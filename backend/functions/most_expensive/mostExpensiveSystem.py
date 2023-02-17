import requests
from most_expensive.getWholesaleEnergyPrice import *


# Set up the API endpoint URL
base_url = "https://moxieenergydeploy-production.up.railway.app/"

# Send the HTTP request and handle the response
#all_systems = requests.get(base_url + "systems")

all_systems = [{'SYSTEM_ID': 2417, 'SYSTEM_NAME': 'EP - Glasgow University - Garscube - Mary Stewart Building- needs upgrade'}]
#print(all_systems.json())
price_data = None
for system in all_systems:
    all_sensors = requests.get(base_url + f"systems/{ system['SYSTEM_ID']}/sensors").json()
    total_for_sensor = 0
    for sensor in all_sensors:
        print(sensor['SENSOR_ID'])
        sensor_data = requests.get(base_url + f"systems/{system['SYSTEM_ID']}/sensors/{sensor['SENSOR_ID']}")

    # ASSUMPTION OF A LIST OF TUPLES EACH WITH A DATE AND A VALUE
        
        oldest_date_formatted = dt.datetime.strftime(sensor_data[-1]["READING_DATE"], "%d-%m-%Y")
        most_recent_date_formatted = dt.datetime.strftime(sensor_data[0]["READING_DATE"], "%d-%m-%Y")
        if price_data is None:
            price_data = getWholesaleEnergyPrice(oldest_date_formatted, most_recent_date_formatted)
    # ASSUMPTION OF DATE/VALUE NOW FORMATTED TO (N,96,2) WHERE N IS NUMBER OF DAYS

        










