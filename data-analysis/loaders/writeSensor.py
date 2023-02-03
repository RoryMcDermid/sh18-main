from helpers.getSingleSensor import get_single_sensor
import json

def write_to_file(system_id=3046, sensor_id='6316312'):
    single_sensor = get_single_sensor(system_id, sensor_id)
    json_object = json.dumps(single_sensor, indent=4)
    with open(f"data/sensor_{sensor_id}.json", "w") as f:
        f.write(json_object)