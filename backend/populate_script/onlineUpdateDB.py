import mysql.connector
from datetime import datetime
import datetime as dt
from helpers.updateFromDates import *
from helpers.getSensorList import *
from helpers.getSystemsList import *
from helpers.createSensorsForSystem import *
from helpers.updateFromDates import *
import os
import dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
dotenv.load_dotenv(dotenv_path=env_path)

mydb = mysql.connector.connect(
    username=os.environ.get('DB_USERNAME'),
    host=os.environ.get('DB_HOST'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB')
)
cursor = mydb.cursor(buffered=True)

cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")
system_ids = [system[0] for system in cursor.fetchall()]
cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_ids[0]}")
sensor_id = cursor.fetchone()[0]
cursor.execute(
    f"SELECT * FROM READINGS_FOR_{sensor_id} ORDER BY(READING_DATE) DESC")

start_date = cursor.fetchone()[0]
end_date = dt.datetime.now() - dt.timedelta(minutes=15)

systems_with_list_of_sensors = {}
reference_time = dt.datetime.now()
for system_id in system_ids:

    if (dt.datetime.now() - reference_time).total_seconds() > 13:
        mydb = mysql.connector.connect(
            username="wod2dh1e3jfuxs210ykt",
            host="aws-eu-west-2.connect.psdb.cloud",
            password="pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
            database="moxie_live"
        )
        cursor = mydb.cursor(buffered=True)
        reference_time = dt.datetime.now()

    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
    systems_with_list_of_sensors[system_id] = [
        sensor_id[0] for sensor_id in cursor.fetchall()]

updateFromDates(start_date, end_date,
                systems_with_list_of_sensors, mydb, cursor, True)