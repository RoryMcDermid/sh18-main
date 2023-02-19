from typing import Dict
import json
import mysql.connector
from helpers import get_single_sensor


def load_from_file(sensor_id='6316312'):
    with open(f'data/sensor_{sensor_id}.json', 'r') as f:
        sensor_data = json.load(f) 
    return sensor_data


def load_from_API(system_id=3046, sensor_id='6316312'):
    single_sensor = get_single_sensor(system_id, sensor_id)
    json_object = json.dumps(single_sensor, indent=4)
    return json_object


def load_from_db(sensor_id='6316312'):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "password",
        database = "moxie_energy"
        )

    cursor = mydb.cursor(buffered=True)

    cursor.execute(f'SELECT SYSTEM_ID FROM SENSOR_SYSTEM_PAIRS WHERE SENSOR_ID = {sensor_id}')
    system_id = cursor.fetchall()[0]

    cursor.execute(f'SELECT * FROM READINGS_FOR_{sensor_id}')
    sensor_readings = [x[0] for x in cursor.fetchall()]
    return sensor_readings

    

