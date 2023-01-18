import mysql.connector
from helpers.getSensorList import *

def get_systems_sensor_list_online(system_ids, mydb, cursor):

  for system_id in system_ids:
    cursor.execute(f"DROP TABLE IF EXISTS SENSORS_FOR_{system_id}")

    sql =f'''CREATE TABLE SENSORS_FOR_{system_id}(
    SENSOR_ID VARCHAR(15) NOT NULL PRIMARY KEY,
    SYSTEM_ID INT NOT NULL,
    )'''
    cursor.execute(sql)

  
  sensorsBySystem = getSensors(system_ids)


  for (system, sensors) in sensorsBySystem.items():

    vals = ''
    for idx, sensor_object in enumerate(sensors):
      sensor_id = sensor_object['sensor_id']
      system_id = sensor_object['system_id']
      if idx != 0:
        vals += ','
      vals += f'({sensor_id}, {system_id})'
    
    sql = f"INSERT INTO SENSORS_FOR_{system} (SENSOR_ID, SYSTEM_ID) VALUES {vals}"
    cursor.execute(sql, vals)
    mydb.commit()
    
  return sensorsBySystem

 




def get_systems_sensor_list(system_ids, mydb, cursor):

  for system_id in system_ids:
    cursor.execute(f"DROP TABLE IF EXISTS SENSORS_FOR_{system_id}")

    sql =f'''CREATE TABLE SENSORS_FOR_{system_id}(
    SENSOR_ID VARCHAR(15) NOT NULL PRIMARY KEY,
    SYSTEM_ID INT NOT NULL,
    SENSOR_TYPE INT NOT NULL,
    SENSOR_MEASUREMENT VARCHAR(40) NOT NULL,
    SENSOR_UNIT VARCHAR(5) NOT NULL
  )'''
    cursor.execute(sql)

  sensors = getSensors(system_ids)

  sensor_ids = sensors.keys()
  sensor_types = []
  system_ids = []
  measurement_types = []
  sensor_units = []


  for sensor in sensors:

    sensor_types.append(sensors[sensor]["type_id"])
    system_ids.append(int(sensors[sensor]["system_id"]))
    measurement_types.append(list(sensors[sensor]["units"].keys())[0])
    sensor_units.append(list(sensors[sensor]["units"].values())[0])

  for sensor_id, system_id, sensor_type, measurement_type, sensor_unit in zip(sensor_ids, system_ids, sensor_types, measurement_types, sensor_units):
      sql = f"INSERT INTO SENSORS_FOR_{system_id} (SENSOR_ID, SYSTEM_ID, SENSOR_TYPE, SENSOR_MEASUREMENT, SENSOR_UNIT) VALUES (%s, %s, %s, %s, %s)"
      vals = (sensor_id, system_id, sensor_type, measurement_type, sensor_unit)
      cursor.execute(sql, vals)
      mydb.commit()
  
  systems_with_sensors_dict = {}
  for system_id in system_ids:
    sql = f'''
  SELECT SENSOR_ID 
  FROM SENSORS_FOR_{system_id}  
  '''
    cursor.execute(sql)
    systems_with_sensors_dict[system_id] = list(map(lambda x: x[0], cursor.fetchall()))
  return systems_with_sensors_dict
