import datetime as dt
from helpers.updateFromDates import *
import psycopg2

connection_string = "postgresql://moxie:iYmwQU_OL2HI1-fiiOqSuQ@fooled-dolphin-7094.8nj.cockroachlabs.cloud:26257/moxie_data?sslmode=verify-full"
mydb = psycopg2.connect(connection_string)
cursor = mydb.cursor()

cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")
system_ids = [system[0] for system in cursor.fetchall()]
cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_ids[0]}")
sensor_id = cursor.fetchone()[0]
cursor.execute(
    f"SELECT * FROM READINGS_FOR_{sensor_id} ORDER BY(READING_DATE) DESC")

row_for_start = cursor.fetchone()
start_date = dt.datetime.combine(row_for_start[0], row_for_start[1])
end_date = dt.datetime.now() - dt.timedelta(minutes=15)

systems_with_list_of_sensors = {}
for system_id in system_ids:

    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
    systems_with_list_of_sensors[system_id] = [
        sensor_id[0] for sensor_id in cursor.fetchall()]
    
updateFromDates(start_date, end_date, systems_with_list_of_sensors, mydb, cursor)