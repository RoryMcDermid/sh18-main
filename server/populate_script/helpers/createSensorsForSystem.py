import mysql.connector
from helpers.getSensorList import *

def get_systems_sensor_list_online(system_ids, mydb, cursor):

  for system_id in system_ids:
    cursor.execute(f"DROP TABLE IF EXISTS SENSORS_FOR_{system_id}")

    sql =f'''CREATE TABLE SENSORS_FOR_{system_id}(
    SENSOR_ID VARCHAR(15) NOT NULL PRIMARY KEY,
    SYSTEM_ID INT NOT NULL
    )'''
    cursor.execute(sql)

  
  sensorsBySystem = getSensors(system_ids)


  for (system, sensors) in sensorsBySystem.items():

    vals = []
    for idx, sensor_object in enumerate(sensors):
      sensor_id = sensor_object['sensor_id']
      system_id = sensor_object['system_id']
      vals.append((sensor_id, system_id))
    
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
    SENSOR_MEASUREMENT VARCHAR(5)
    )'''
    cursor.execute(sql)

  sensorsBySystem = getSensors(system_ids)

  for system, sensors in sensorsBySystem.items():

    vals = []
    for idx, sensor_object in enumerate(sensors):
      sensor_id = sensor_object['sensor_id']
      system_id = system
      measurement_type = list(sensor_object["units"].values())[0]
      vals.append((sensor_id, system_id, measurement_type))
    
    if len(vals) > 0:
      print(vals, system)
      sql = f"INSERT INTO SENSORS_FOR_{system} (SENSOR_ID, SYSTEM_ID, SENSOR_MEASUREMENT) VALUES (%s, %s, %s)"
      cursor.executemany(sql, vals)
      mydb.commit()
    else:
      print("0")
      cursor.execute(f"DROP TABLE SENSORS_FOR_{system}")
      mydb.commit()
      cursor.execute(f"DELETE FROM SYSTEMS WHERE SYSTEM_ID = {system} ")
      mydb.commit()
  return sensorsBySystem
