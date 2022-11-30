import mysql.connector
import datetime as dt
from helpers.getDataFromDates import *
from helpers.pushDownIteration import *
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *

create_db()
create_systems()

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor()

# SELECT SYSTEM ID TO GET ITS SENSORS
system_id = 2442
sensor_list = get_systems_sensor_list(system_id)

setup_end_date = dt.datetime.now() - dt.timedelta(days=1)
setup_start_date = setup_end_date - dt.timedelta(weeks=2)

for sensor in sensor_list:

  readings_from_dates = getDatafromDates(setup_start_date, setup_end_date, system_id, sensor)
  cursor.execute(f"DROP TABLE IF EXISTS ITER_1_{sensor}")

  sql =f'''CREATE TABLE ITER_1_{sensor}(
    DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
    VALUE DECIMAL(9,6) NOT NULL
  )'''
  cursor.execute(sql)


  for result in readings_from_dates:
      
      date, reading = result["date"], result["reading"]
      sql = f"INSERT INTO ITER_1_{sensor} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
      vals = (date, reading)
      cursor.execute(sql, vals)
  mydb.commit()

  iter_list = ["ITER_2", "ITER_3", "ITER_4"]
  # Loop through each possible iteration, passing what one you are working on into a separate function.
  for iter_val in iter_list:
      sql =f'''CREATE TABLE {iter_val + '_' + sensor}(
        DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
        VALUE DECIMAL(9,6) NOT NULL
        )'''
      cursor.execute(sql)
      pushDownIteration(iter_val, sensor)







