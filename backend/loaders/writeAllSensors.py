from typing import List
from helpers import get_sensors_by_system
import json

def write_all_sensors_to_file(system_IDs: List[str]):
    all_sensors = get_sensors_by_system(system_IDs)
    json_object = json.dumps(all_sensors, indent=4) 
    with open("data/all_sensors.json", "w") as outfile:
        outfile.write(json_object)