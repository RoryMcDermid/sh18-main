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
# Current system id actually covers all sensors available in Uni, 
# so we can get all data in one go.
#Once populateDB.py has been called once, we will no longer have to call it and only use updateDB.py.
system_id = 2542
sensor_list = get_systems_sensor_list(system_id)


#Setup the dates that we are looking to record from.
#This takes yesterday as the most recent date and goes 1 week back from there
#to get the data from.
#The reasom for ending at yesterday is to allow for the updateDB.py file to be called to
#Show that it is working.

setup_end_date = dt.datetime.now() - dt.timedelta(days=1)
setup_start_date = setup_end_date - dt.timedelta(weeks=1)
readings_from_dates = getDatafromDates(setup_start_date, setup_end_date, system_id, sensor_list)

#from all the data received, place it into the appropriate first iteration table in the database.
#We will only ever add to the first iteration table directly from calls from the database and then
# 'push down' the appropriate summed values to the next iterations.
for i in range(len(sensor_list)):

  cursor.execute(f"DROP TABLE IF EXISTS ITER_1_{sensor_list[i]}")

  sql =f'''CREATE TABLE ITER_1_{sensor_list[i]}(
    DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
    VALUE DECIMAL(11,6) NOT NULL
  )'''
  cursor.execute(sql)

  for result in readings_from_dates[i]:
      
      date, reading = result["date"], result["reading"]
      sql = f"INSERT INTO ITER_1_{sensor_list[i]} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
      vals = (date, reading)
      cursor.execute(sql, vals)
  mydb.commit()

  iter_list = ["ITER_2", "ITER_3", "ITER_4"]
  # Loop through each possible iteration, passing what one you are working on into a separate function.
  # This is where the push down of data occurs.
  for iter_val in iter_list:
      sql =f'''CREATE TABLE {iter_val + '_' + sensor_list[i]}(
        DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
        VALUE DECIMAL(11,6) NOT NULL
        )'''
      cursor.execute(sql)
      pushDownIteration(iter_val, sensor_list[i])







