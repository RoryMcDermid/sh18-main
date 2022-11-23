import mysql.connector
from GetListOfSystems import *

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS SYSTEMS")

sql ='''CREATE TABLE SYSTEMS(
   SYSTEM_ID INT NOT NULL PRIMARY KEY,
   SYSTEM_NAME VARCHAR(150) NOT NULL,
   SENSOR_COUNT INT NOT NULL
)'''
cursor.execute(sql)

systems_list = getSystemsList()

system_ids = []
system_names = []
system_sensor_count = []

for system in systems_list:
    system_ids.append(system)
    system_names.append(systems_list[system]["name"])
    system_sensor_count.append(systems_list[system]["noOfSensors"])

for system_id, name, sensor_count in zip(system_ids, system_names, system_sensor_count):
    sql = "INSERT INTO SYSTEMS (SYSTEM_ID, SYSTEM_NAME, SENSOR_COUNT) VALUES (%s, %s, %s)"
    vals = (system_id, name, sensor_count)
    cursor.execute(sql, vals)
    mydb.commit()

