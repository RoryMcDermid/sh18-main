from typing import List
from helpers.getSensors import getSensors
import json

def write_all_sensors_to_file(system_IDs: List[str]):
    all_sensors = getSensors(system_IDs)
    json_object = json.dumps(all_sensors, indent=4) 
    with open("data/all_sensors.json", "w") as outfile:
        outfile.write(json_object)