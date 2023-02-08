import mysql.connector
import datetime as dt
from helpers.getDataForBaseline import *
import json

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)
cursor = mydb.cursor( buffered=True)

# This has been set up to currently only access and create the baseline and features
# tables for the sensors belonging to system 2417. The code that has been commented out
# can be used to then create these tables for all sensors.

# cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")
# system_ids = [system[0] for system in cursor.fetchall()]
# cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_ids[0]}")
# sensor_id = cursor.fetchone()[0]

cursor.execute("SELECT SENSOR_ID FROM SENSORS_FOR_2417")
systems_with_list_of_sensors = {}
# for system_id in system_ids:
#     cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
#     systems_with_list_of_sensors[system_id] = [sensor_id[0] for sensor_id in cursor.fetchall()]
systems_with_list_of_sensors[2417] = [sensor_id[0] for sensor_id in cursor.fetchall()]

# We are looking to set up the tables with a good amount of data,
# so the function requests a year's worth of backlog data from the 
# API which will then be parsed and formatted to be added to the database.
# This is the main reason why it is currently set up to only have a limited number of 
# sensors being requested as doing it for all would be very taxing in a computational
# sense. 
yesterday_pre_midnight = dt.datetime.combine(dt.date.today(), dt.datetime.min.time()) - dt.timedelta(minutes=15)
year_ago = yesterday_pre_midnight - dt.timedelta(weeks=52)

all_year_data_resp = getDataForBaseline(year_ago, yesterday_pre_midnight, systems_with_list_of_sensors)

for i in range(len(all_year_data_resp["systems"])):
    system_id = all_year_data_resp["systems"][i]["system_id"]
    for j in range(len(all_year_data_resp["systems"][i]["sensors"])):

        sensor_id = all_year_data_resp["systems"][i]["sensors"][j]["sensor_id"]
        cursor.execute(f"DROP TABLE IF EXISTS FEATURES_FOR_{sensor_id}")
        mydb.commit()
        cursor.execute(f"""CREATE TABLE FEATURES_FOR_{sensor_id}(
                        TIME_SLOT TIME NOT NULL PRIMARY KEY,
                        BASELINE DECIMAL(15,6) NOT NULL,
                        AVERAGE DECIMAL(15,6) NOT NULL
                        )""")
        mydb.commit()

        cursor.execute(f"SELECT SENSOR_MEASUREMENT FROM SENSORS_FOR_{system_id} WHERE SENSOR_ID = {sensor_id}")
        sensor_measurement = cursor.fetchall()[0][0] 
        readings = all_year_data_resp["systems"][i]["sensors"][j]["data"]
        baseline_avg_for_sensor = {}

        for reading in readings:
            new_val = reading["values"][sensor_measurement] 
            time_slot = reading["record_date"][11:16]

            # Zero values would have to severe an impact on the baseline,
            # so these are avoided.
            if new_val > 0:
                if  time_slot not in baseline_avg_for_sensor:
                    new_val = reading["values"][sensor_measurement] 
                    baseline_avg_for_sensor[time_slot] = {"baseline": new_val, "average": new_val}

                elif new_val < baseline_avg_for_sensor[time_slot]["baseline"]:
                    baseline_avg_for_sensor[time_slot]["baseline"] = new_val

                new_average = (baseline_avg_for_sensor[time_slot]["average"] + new_val)/2
                baseline_avg_for_sensor[time_slot]["average"] = new_average
        
        
        for time_slot, base_and_avg in baseline_avg_for_sensor.items():
            sql = f"INSERT INTO FEATURES_FOR_{sensor_id} VALUES (%s,%s,%s)"
            baseline = base_and_avg["baseline"]
            average = base_and_avg["average"]

            cursor.execute(sql, (dt.datetime.strptime(time_slot, "%H:%M").time(), baseline, average))
        mydb.commit()


