from helpers.getSingleSensor import get_single_sensor
import json


def load_from_file(sensor_id='6316312'):
    with open(f'data/sensor_{sensor_id}.json', 'r') as f:
        sensor_data = json.load(f) 
    return sensor_data


def load_from_API(system_id=3046, sensor_id='6316312'):
    single_sensor = get_single_sensor(system_id, sensor_id)
    json_object = json.dumps(single_sensor, indent=4)
    return json_object
