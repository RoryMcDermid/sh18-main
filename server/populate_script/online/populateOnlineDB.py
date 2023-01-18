import mysql.connector
import datetime as dt
from helpers.getDataFromDates import *
from helpers.pushDownIteration import *
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *

TIME_PERIOD = 2

mydb = mysql.connector.connect(
  host = "us-east.connect.psdb.cloud",
  user = "1dq43m1k3cumbcauts87",
  password = "pscale_pw_3wMy14IDYxWEDFMiNm42fQIZ9p0RooayTZpiKtf6yND",
  database = "test-db"
)


cursor = mydb.cursor()

system_ids = create_systems(mydb, cursor)

#return a dictionary where the keys are the system ids, and
#the values are the sensors associated with that system
systems_with_sensors_dict = get_systems_sensor_list_online(system_ids, mydb, cursor)
systems_with_sensors_dict.pop(2542)

for system, sensors in systems_with_sensors_dict.items():
  if len(sensors) == 0:
    mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM SYSTEMS WHERE SYSTEM_ID = {system} ")
    mydb.commit()

mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)
cursor = mydb.cursor()

#Setup the dates that we are looking to record from.
#This takes yesterday as the most recent date and goes 2 days back from there
#to get the data from.
#The reasom for ending at yesterday is to allow for the updateDB.py file to be called to
#Show that it is working.

setup_end_date = dt.datetime.now() - dt.timedelta(days=1)
setup_start_date = setup_end_date - dt.timedelta(days=TIME_PERIOD)

#a dictionary is returned which has the sensor ids as the key, and the associated
#data values from specified time period as the values in a list of dictionaries with
#each dict having a date and reading key, with appropriate values.

sensors_dates_and_vals = getDatafromDatesOnline(setup_start_date, setup_end_date, systems_with_sensors_dict, mydb, cursor)

#from all the data received, place it into the appropriate first iteration table in the database.
#We will only ever add to the first iteration table directly from calls from the database and then
# 'push down' the appropriate summed values to the next iterations.

iter_list = ["ITER_2", "ITER_3", "ITER_4"]
#looking at each system
for i in range(len(systems_with_sensors_dict)):
  systems = list(systems_with_sensors_dict.keys())
  system = systems[i]
  #looking at each sensor in that system
  for j in range(len(systems_with_sensors_dict[system])):
    mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)
    cursor = mydb.cursor()
      
    sensor_id = systems_with_sensors_dict[system][j]

    cursor.execute(f"DROP TABLE IF EXISTS ITER_1_{system}_{sensor_id}")
    mydb.commit()

    sql =f'''CREATE TABLE ITER_1_{system}_{sensor_id}(
    DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
    VALUE DECIMAL(15,6) NOT NULL
  )'''
    print("Add table?")
    cursor.execute(sql)
    mydb.commit()

    #add all sensor id values from dictionary
    for result in sensors_dates_and_vals[sensor_id]:
      
      date, reading = result["date"], result["reading"]
      sql = f"INSERT INTO ITER_1_{system}_{sensor_id} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
      vals = (date, reading)
      cursor.execute(sql, vals)
      mydb.commit()

    #return all values from newly created table
    cursor.execute(f"SELECT * FROM ITER_1_{system}_{sensor_id}")
    vals = cursor.fetchall()
    print(vals)
    sum_of_vals = sum(list(map(lambda x: x[1], vals)))
    #if the table is empty, delete table for sensor and 
    #delete sensor from associated system table
    if len(vals) == 0 or sum_of_vals == 0:
      cursor.execute(f"DROP TABLE ITER_1_{system}_{sensor_id}")
      mydb.commit()
      cursor.execute(f"DELETE FROM SENSORS_FOR_{system} WHERE SENSOR_ID = {sensor_id}")
      mydb.commit()
    else:
        
      for iter_val in iter_list:
       
        mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)
        cursor = mydb.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {iter_val}_{system}_{sensor_id}")
        mydb.commit()
       
        sql =f'''CREATE TABLE {iter_val}_{system}_{sensor_id}(
    DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
    VALUE DECIMAL(15,6) NOT NULL
  )'''
        cursor.execute(sql)
        mydb.commit()
        print("Table should be made")
        pushDownIterationOnline(iter_val, sensor_id, system, mydb, cursor)


mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)
cursor = mydb.cursor()

cursor.execute(f"SHOW TABLES")
tables = cursor.fetchall()

for table in tables:
  mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)
  cursor = mydb.cursor()
  sql = f'''SELECT COUNT(*) 
            FROM {table[0]}'''
  cursor.execute(sql)
  if cursor.fetchall()[0][0] == 0:
    cursor.execute(f"DROP TABLE {table[0]}")
