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

def get_systems_sensor_list(system_ids, mydb, cursor, mock=0):

  if mock == 0:
    sensorsBySystem = getSensors(system_ids)
  else:
    sensorsBySystem = mock

  cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")
  stored_systems = set(x[0] for x in cursor.fetchall())
  returned_systems = set(sensorsBySystem.keys())
  stored_systems.difference_update(returned_systems)

  for void_system in stored_systems:
    cursor.execute(f"DELETE FROM SYSTEMS WHERE SYSTEM_ID = {void_system}")
    mydb.commit()
  cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")

  
  systems_with_list_of_sensors = {}
  added_sensors = set()

  for system, sensors in sensorsBySystem.items():

    set_of_sensors = set(x["sensor_id"] for x  in sensors)
    set_of_sensors.difference_update(added_sensors)
    
    if len(set_of_sensors) > 0:
      systems_with_list_of_sensors[int(system)] = []
      vals = []
      for idx, sensor_object in enumerate(sensors):
        sensor_id = sensor_object['sensor_id']
        if sensor_id not in added_sensors:
          added_sensors.add(sensor_id)
          system_id = system
          measurement_type = list(sensor_object["units"].keys())[0]
          vals.append((sensor_id, system_id, measurement_type))
          systems_with_list_of_sensors[int(system)].append(sensor_id)
    

      sql =f'''CREATE TABLE SENSORS_FOR_{system_id}(
          SENSOR_ID VARCHAR(15) NOT NULL PRIMARY KEY,
          SYSTEM_ID INT NOT NULL,
          SENSOR_MEASUREMENT VARCHAR(40)
            )'''
      cursor.execute(sql)
      mydb.commit()

      sql = f"INSERT INTO SENSORS_FOR_{system} (SENSOR_ID, SYSTEM_ID, SENSOR_MEASUREMENT) VALUES (%s, %s, %s)"
      cursor.executemany(sql, vals)
      mydb.commit()
    else:
      cursor.execute(f"DELETE FROM SYSTEMS WHERE SYSTEM_ID = {system}")
      mydb.commit()
  return systems_with_list_of_sensors

def get_systems_sensor_list_no_creation(system_ids, mydb, cursor, mock=0):

  if mock == 0:
    sensorsBySystem = getSensors(system_ids)
  else:
    sensorsBySystem = mock

    systems_with_list_of_sensors = {}

  for system, sensors in sensorsBySystem.items():
    system_ids.remove(int(system))
    systems_with_list_of_sensors[int(system)] = []
    
    if len(sensors) > 0:
      vals = []
      for idx, sensor_object in enumerate(sensors):

        sensor_id = sensor_object['sensor_id']
        system_id = system
        measurement_type = list(sensor_object["units"].keys())[0]
        vals.append((sensor_id, system_id, measurement_type))
        systems_with_list_of_sensors[int(system)].append(sensor_id)

  return systems_with_list_of_sensors
