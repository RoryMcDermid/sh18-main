import os
from helpers.getSingleSensor import get_single_sensor
import json

def write_multiple_sensors_to_files(system_id=2417):
    with open('data/systems_to_sensors.json', 'r') as f:
        systems_dict = json.load(f)

    system_sensors = systems_dict[str(system_id)]
    for sensor_id in system_sensors:
        single_sensor = get_single_sensor(system_id, sensor_id)
        json_object = json.dumps(single_sensor, indent=4)
        if not os.path.exists(f"data/sensor_{sensor_id}.json"):
            with open(f"data/sensor_{sensor_id}.json", "w") as f:
                f.write(json_object)


