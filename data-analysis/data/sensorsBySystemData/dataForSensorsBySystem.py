import mysql.connector
import json
import datetime as dt

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor( buffered=True)

chosen_systems = [2542, 2418, 2417, 2441]

returned_data = {}

for system in chosen_systems:
    returned_data[system] = {}
    cursor.execute(f"""SELECT SENSOR_ID FROM SENSOR_SYSTEM_PAIRS 
                        WHERE SYSTEM_ID = {system}""")
    sensors = [x[0] for x in cursor.fetchall()]
    for sensor_id in  sensors:
        cursor.execute(f"""SELECT * FROM READINGS_FOR_{sensor_id}""")
        queried_data = cursor.fetchall()
        returned_data[system][sensor_id] = [(x[0].strftime("%Y-%m-%dT%H:%M:%S"), float(x[1])) for x in queried_data] 

json_object = json.dumps(returned_data)
 
# Writing to sample.json
with open("sensorsBySystemData.json", "w") as outfile:
    outfile.write(json_object)