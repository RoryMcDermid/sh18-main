from helpers.getSensorList import *
import mysql.connector
import datetime as dt

def get_systems_sensor_list(system_ids, mydb, cursor, mock=0, online=False):

  # Connect to online DB to avoid timeout.
  if online:
    mydb = mysql.connector.connect(
        username = "wod2dh1e3jfuxs210ykt",
        host = "aws-eu-west-2.connect.psdb.cloud",
        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
        database = "moxie_live"
        )
    cursor = mydb.cursor(buffered=True)

  # Use mock to avoid API call if mock is available,
  # otherwise make API call using getSensors function.
  if mock == 0:
    sensorsBySystem = getSensors(system_ids)
  else:
    sensorsBySystem = mock

  # Some systems have no associated sensors so they are not returned
  # from the API call. For this reason we remove these systems from the
  # SYSTEMS table in the database.
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
  
  if online:
    reference_time = dt.datetime.now()

  for system, sensors in sensorsBySystem.items():

    #Connect to online DB each time to avoid timeouts.
    if online:
      if (dt.datetime.now() - reference_time).total_seconds() > 13:
        mydb = mysql.connector.connect(
                        username = "wod2dh1e3jfuxs210ykt",
                        host = "aws-eu-west-2.connect.psdb.cloud",
                        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
                        database = "moxie_live"
                        )
        cursor = mydb.cursor(buffered=True)
        reference_time = dt.datetime.now()

    # Check to see if this system has any unique sensors not already
    # added to another system.
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