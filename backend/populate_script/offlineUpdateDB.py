import mysql.connector
from datetime import datetime
import datetime as dt
from helpers.getSensorList import *
from helpers.getSystemsList import *
from helpers.createSensorsForSystem import *
from helpers.updateFromDates import *

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "moxie_energy"
)
cursor = mydb.cursor(buffered=True)

cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")
system_ids = [system[0] for system in cursor.fetchall()]
cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_ids[0]}")
sensor_id = cursor.fetchone()[0]
# This hardcoded variable is only here so I can access a value from the above returned dictionary.
cursor.execute(f"SELECT * FROM READINGS_FOR_{sensor_id} ORDER BY(READING_DATE) DESC")

start_date = cursor.fetchone()[0]
end_date = dt.datetime.now() - dt.timedelta(minutes=15)

systems_with_list_of_sensors = {}
for system_id in system_ids:
    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
    systems_with_list_of_sensors[system_id] = [sensor_id[0] for sensor_id in cursor.fetchall()]

updateFromDates(start_date, end_date, systems_with_list_of_sensors, mydb, cursor)