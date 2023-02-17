import mysql.connector
import datetime as dt

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)
cursor = mydb.cursor( buffered=True)

chosen_systems = [ 2417, 2418]

count_of_system_sensors = {}
all_returned_sensors = []

for system in chosen_systems:
    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system}")
    sensor_ids = [x[0] for x in cursor.fetchall()]
    count_of_system_sensors[system] = len(sensor_ids)
    all_returned_sensors += sensor_ids


print(count_of_system_sensors)
print(all_returned_sensors)
today_midnight = dt.datetime.combine(dt.datetime.now().date(), dt.datetime.min.time())
print(today_midnight)

cursor.execute(f"SELECT * FROM READINGS_FOR_{all_returned_sensors[0]} WHERE READING_DATE < %s", (today_midnight, ))
print(cursor.fetchall())

    