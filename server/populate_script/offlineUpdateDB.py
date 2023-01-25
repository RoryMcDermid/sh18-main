import mysql.connector
from datetime import datetime
import datetime as dt
from helpers.updateFromDates import *
from helpers.getSensorList import *
from helpers.getSystemsList import *
from helpers.createSensorsForSystem import *

#This function finds the date of the most recently stored value in the 
#iter_1 table, then gets all the dates from the api using the previously defined function.
#It then performs the push down function, adding all appropriate values to tables that are
#needed. Then remove the unwanted values from tables that are no longer needed to be stored in
#the specified time ranges for each iteration.

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
cursor.execute(f"SELECT * FROM ITER_1_{sensor_id} ORDER BY(DATE_OF_RECORD) DESC")

most_recent_record_date = cursor.fetchone()[0]
current_date = dt.datetime.now()

systems_with_list_of_sensors = {}
for system_id in system_ids:
    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
    systems_with_list_of_sensors[system_id] = [sensor_id[0] for sensor_id in cursor.fetchall()]

updateFromDates(most_recent_record_date, current_date,  systems_with_list_of_sensors, mydb, cursor)