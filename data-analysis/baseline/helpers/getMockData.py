from getSingleSensor import getSingleSensor
from getSensors import getSensors
from getSystemsList import getSystems
import json


# loads systems from file, extracts IDs, 
# and gets back and writes sensors to a file

def loader():
    with open('data/all_systems.json', 'r') as f:
        all_systems = json.load(f)

    system_IDs = []
    for system_id in all_systems.keys():
        system_IDs.append(int(system_id))
    
    all_sensors = getSensors(system_IDs)
    json_object = json.dumps(all_sensors, indent=4) 
    with open("data/all_sensors.json", "w") as outfile:
        outfile.write(json_object)

    single_sensor = getSingleSensor(system_id=3046, sensor_id='6316312')
    json_object = json.dumps(single_sensor, indent=4)
    with open("data/single_sensor.json", "w") as f:
        f.write(json_object)


print('hello')